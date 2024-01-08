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
    GAMEPLAY_DICT,
    OPACITY_ON_BUTTON_PRESS,
    MAX_NB_LEVELS_PER_BRANCH,
    LEVEL_BUTTON_SIZE_HINT,
    LEVEL_BUTTON_SPACING
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
            release_function=lambda: 1 + 1,
            is_unlocked=False,
            **kw):
        super().__init__(**kw)
        self.release_function = release_function
        self.always_release = True
        self.is_unlocked = is_unlocked
        self.level_id = level_id
        self.level_label_text = str(level_id)

    def on_press(self):
        if not self.disable_button:
            self.opacity = OPACITY_ON_BUTTON_PRESS

    def on_release(self):
        if not self.disable_button:
            self.release_function()
            self.opacity = 1


class LevelBranch(RelativeLayout):
    def __init__(
            self,
            act_id,
            branch_id,
            **kw):
        super().__init__(**kw)
        self.act_id = act_id
        self.branch_id = branch_id

    def compute_level_button_coords(self, local_id):
        if self.branch_id % 2 == 0:
            # center_x = LEVEL_BUTTON_SIDE_OFFSET + (LEVEL_BUTTON_SIZE_HINT + LEVEL_BUTTON_SIDE_OFFSET) * \
            #     local_id + LEVEL_BUTTON_SIZE_HINT / 2
            center_y = ...
        else:
            center_x = ...
            center_y = ...
        return center_x, center_y

    def build_layout(self):
        # Find the number of levels contained in the branch, cannot be greater than MAX_NB_LEVELS_PER_BRANCH
        nb_levels = len(GAMEPLAY_DICT[self.act_id]) - 1
        self.local_nb_levels = (nb_levels - self.branch_id * MAX_NB_LEVELS_PER_BRANCH)\
            % MAX_NB_LEVELS_PER_BRANCH
        for local_id in range(self.local_nb_levels):
            level_id = local_id + 1 + self.branch_id * MAX_NB_LEVELS_PER_BRANCH
            center_x, center_y = self.compute_level_button_coords(local_id)
            level_is_unlocked = ...
            level_nb_stars = ...
