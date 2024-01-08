"""
Module to create the game screen.
"""

###############
### Imports ###
###############

### Kivy imports ###

from kivy.properties import (
    StringProperty,
    NumericProperty
)

### Local imports ###

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


class GameScreen(ImprovedScreen):
    """
    Class to manage the game screen.
    """

    current_level_name = StringProperty()
    nb_stars = NumericProperty()

    def __init__(self, **kwargs) -> None:
        current_theme_image = USER_DATA.settings["current_theme_image"]
        super().__init__(
            back_image_path=PATH_BACKGROUNDS +
            THEMES_DICT[current_theme_image]["image"],
            **kwargs)
        self.current_act_id = ""

    def on_enter(self, *args):
        temp = self.current_act_id.replace("Act", "")
        self.current_level_name = "Act " + temp + " – " + "1"
        self.load_game_play()
        self.load_game_user()
        return super().on_enter(*args)

    def load_game_play(self):
        pass

    def load_game_user(self):
        pass
