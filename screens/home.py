"""
Module to create the home screen.
"""

###############
### Imports ###
###############

from tools.constants import (
    SCREEN_TITLE,
    SCREEN_BOTTOM_BAR
)
from tools.kivy_tools import (
    LinconymScreen
)
from tools import (
    music_mixer
)


#############
### Class ###
#############


class HomeScreen(LinconymScreen):
    """
    Class to manage the home screen which contains the buttons to launch the free and daily modes.
    """

    dict_type_screen = {
        SCREEN_TITLE : "Linconym",
        SCREEN_BOTTOM_BAR : "home"
    }

    def open_classic_mode(self):
        """
        Open the classic mode screen.
        """
        self.manager.go_to_next_screen(next_screen_name="classic_mode")
