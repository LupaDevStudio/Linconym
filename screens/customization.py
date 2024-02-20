"""
Module to create the customization screen.
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


class CustomizationScreen(ImprovedScreen):
    """
    Class to manage the customization screen which allows the user to choose between themes or music.
    """

    def __init__(self, **kwargs) -> None:
        current_theme_image = USER_DATA.settings["current_theme_image"]
        super().__init__(
            back_image_path=PATH_BACKGROUNDS +
            THEMES_DICT[current_theme_image]["image"],
            **kwargs)

    def on_enter(self, *args):
        return super().on_enter(*args)

    def open_musics_screen(self, *_):
        self.go_to_next_screen(screen_name="musics")

    def open_themes_screen(self, *_):
        self.go_to_next_screen(screen_name="themes")
