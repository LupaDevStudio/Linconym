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
from tools import (
    music_mixer
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
        current_music = USER_DATA.settings["current_music"]
        if music_mixer.musics[current_music].state == "stop":
            music_mixer.play(current_music, loop=True)
        current_theme_image = USER_DATA.settings["current_theme_image"]
        self.set_back_image_path(
            PATH_BACKGROUNDS + THEMES_DICT[current_theme_image]["image"])
        return super().on_enter(*args)

    def open_classic_mode(self):
        """
        Open the classic mode screen.
        """
        self.manager.go_to_next_screen(next_screen_name="classic_mode")
