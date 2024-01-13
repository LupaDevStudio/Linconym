"""
Module to create the levels tree for the levels screen.
"""

###############
### Imports ###
###############

### Kivy imports ###

from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import (
    NumericProperty,
    BooleanProperty,
    ColorProperty,
    StringProperty
)

### Local imports ###
from tools.constants import (
    USER_DATA,
    GAMEPLAY_DICT,
    OPACITY_ON_BUTTON_PRESS,
    MAX_NB_LEVELS_PER_BRANCH,
    LEVEL_BUTTON_SIZE_HINT,
    LEVEL_BUTTON_SPACING,
    LEVEL_BUTTON_SIDE_OFFSET
)


###############
### Classes ###
###############

class LevelButton(ButtonBehavior, RelativeLayout):

    nb_stars = NumericProperty()
    font_ratio = NumericProperty(1)
    level_label_text = StringProperty()
    primary_color = ColorProperty((0.5, 0.5, 0.5, 1))
    secondary_color = ColorProperty((0.2, 0.2, 0.2, 1))
    is_unlocked = BooleanProperty(False)
    disable_button = BooleanProperty(False)

    def __init__(
            self,
            level_id=0,
            is_unlocked=False,
            nb_stars=0,
            **kw):
        super().__init__(**kw)
        self.always_release = True
        self.is_unlocked = is_unlocked
        self.level_id = level_id
        self.level_label_text = str(level_id)
        self.nb_stars = nb_stars

    def on_press(self):
        if not self.disable_button:
            self.opacity = OPACITY_ON_BUTTON_PRESS

    def on_release(self):
        if not self.disable_button:
            self.opacity = 1
            self.get_root_window().children[0].get_screen(
                "game").current_act_id = self.parent.act_id
            self.get_root_window().children[0].get_screen(
                "game").current_level_id = str(self.level_id)
            self.get_root_window().children[0].current = "game"


class LevelBranch(RelativeLayout):

    font_ratio = NumericProperty()

    def __init__(
            self,
            act_id="Act1",
            branch_id=0,
            **kw):
        super().__init__(**kw)
        self.act_id = act_id
        self.branch_id = branch_id
        self.build_layout()

    def compute_level_button_pos_hint(self, local_id: int):
        """
        Compute the pos hint of a level button given its local id.

        Parameters
        ----------
        local_id : int
            Local id of the level button inside the level branch.

        Returns
        -------
        dict
            Position hint dictionnary for the level button.
        """
        pos_hint = {}
        if self.branch_id % 2 == 0:
            center_x = LEVEL_BUTTON_SIDE_OFFSET + (LEVEL_BUTTON_SIZE_HINT + LEVEL_BUTTON_SPACING) * \
                local_id + LEVEL_BUTTON_SIZE_HINT / 2
            if local_id + 1 < MAX_NB_LEVELS_PER_BRANCH:
                pos_hint["top"] = 1
            else:
                pos_hint["y"] = 0
                center_x = center_x - LEVEL_BUTTON_SPACING
        else:
            center_x = 1 - (LEVEL_BUTTON_SIDE_OFFSET + (LEVEL_BUTTON_SIZE_HINT + LEVEL_BUTTON_SPACING) *
                            local_id + LEVEL_BUTTON_SIZE_HINT / 2)
            if local_id == 0:
                pos_hint["top"] = 1
            else:
                pos_hint["y"] = 0
        pos_hint["center_x"] = center_x
        return pos_hint

    def build_layout(self):
        """
        Add all buttons to the layout to build the branch.
        """
        # Find the number of levels contained in the branch, cannot be greater than MAX_NB_LEVELS_PER_BRANCH
        nb_levels = len(GAMEPLAY_DICT[self.act_id]) - 1
        self.local_nb_levels = min(
            nb_levels - self.branch_id * MAX_NB_LEVELS_PER_BRANCH, 4)
        for local_id in range(self.local_nb_levels):
            level_id = local_id + 1 + self.branch_id * MAX_NB_LEVELS_PER_BRANCH
            level_key = str(level_id)
            level_pos_hint = self.compute_level_button_pos_hint(local_id)
            if level_key in USER_DATA.classic_mode[self.act_id]:
                level_is_unlocked = True
                level_nb_stars = USER_DATA.classic_mode[self.act_id][level_key]["nb_stars"]
            else:
                level_is_unlocked = False
                level_nb_stars = 0
            level_button = LevelButton(level_id=level_id,
                                       is_unlocked=level_is_unlocked,
                                       nb_stars=level_nb_stars,
                                       pos_hint=level_pos_hint,
                                       size_hint=(LEVEL_BUTTON_SIZE_HINT, 0.4))
            self.add_widget(level_button)
