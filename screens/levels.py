"""
Module to create the levels screen.
"""

###############
### Imports ###
###############

from tools.path import (
    PATH_BACKGROUNDS
)
from tools.constants import (
    USER_DATA,
    THEMES_DICT
)
from tools.kivy_tools import (
    ImprovedScreen
)
from tools import (
    music_mixer
)


#############
### Class ###
#############


class LevelsScreen(ImprovedScreen):
    """
    Class to manage the levels screen which allow the user to select a level inside an act.
    """

    def __init__(self, **kwargs) -> None:
        current_theme_image = USER_DATA.settings["current_theme_image"]
        super().__init__(
            back_image_path=PATH_BACKGROUNDS +
            THEMES_DICT[current_theme_image]["image"],
            **kwargs)
        self.current_act_id = ""

    def on_enter(self, *args):
        return super().on_enter(*args)
