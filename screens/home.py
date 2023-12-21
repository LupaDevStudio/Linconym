"""
Module to create the home screen.
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


#############
### Class ###
#############


class HomeScreen(ImprovedScreen):
    """
    Class to manage the home screen which contains the buttons to launch the free and daily modes.
    """

    def __init__(self, **kwargs) -> None:
        current_theme_image = USER_DATA.settings["current_theme_image"]
        super().__init__(
            back_image_path=PATH_BACKGROUNDS +
            THEMES_DICT[current_theme_image]["image"],
            **kwargs)

    def on_enter(self, *args):
        current_theme_image = USER_DATA.settings["current_theme_image"]
        self.set_back_image_path(
            PATH_BACKGROUNDS + THEMES_DICT[current_theme_image]["image"])
        return super().on_enter(*args)

    def open_free_mode(self):
        """
        Open the free mode screen.
        """
        self.manager.current = "free_mode"
