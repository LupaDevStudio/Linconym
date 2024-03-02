"""
Module to create the home screen.
"""

###############
### Imports ###
###############

from tools.constants import (
    SCREEN_TITLE,
    SCREEN_BOTTOM_BAR,
    SCREEN_TUTORIAL
)
from tools.kivy_tools import (
    LinconymScreen
)
from tools import (
    music_mixer
)
from tools.constants import (
    USER_DATA
)


#############
### Class ###
#############


class HomeScreen(LinconymScreen):
    """
    Class to manage the home screen which contains the buttons to launch the free and daily modes.
    """

    dict_type_screen = {
        SCREEN_TITLE: "Linconym",
        SCREEN_BOTTOM_BAR: "home",
        SCREEN_TUTORIAL: ""
    }

    def on_enter(self, *args):
        current_music = USER_DATA.settings["current_music"]
        if music_mixer.musics[current_music].state == "stop":
            music_mixer.play(current_music, loop=True)
        return super().on_enter(*args)

    def open_classic_mode(self):
        """
        Open the classic mode screen.
        """
        self.manager.go_to_next_screen(next_screen_name="classic_mode")
