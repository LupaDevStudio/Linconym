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
from tools.path import (
    PATH_TEXT_FONT
)
from tools.constants import (
    GAMEPLAY_DICT,
    OPACITY_ON_BUTTON_PRESS
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

    def build_layout(self):
        # Find the number of levels contained in the branch, cannot be greater than 5
        nb_levels = ...
        self.local_nb_levels = ...
