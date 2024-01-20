"""
Module to create the game screen.
"""

###############
### Imports ###
###############

### Python imports ###

from functools import partial

### Kivy imports ###

from kivy.properties import (
    StringProperty,
    NumericProperty,
    ColorProperty
)

### Local imports ###

from tools.path import (
    PATH_BACKGROUNDS
)
from tools.constants import (
    USER_DATA,
    THEMES_DICT,
    LETTER_FONT_SIZE
)
from tools.kivy_tools import (
    ImprovedScreen,
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
    primary_color = ColorProperty((0, 0, 0, 1))
    secondary_color = ColorProperty((0, 0, 0, 1))

    def __init__(self, **kwargs) -> None:
        current_theme_image = USER_DATA.settings["current_theme_image"]
        super().__init__(
            back_image_path=PATH_BACKGROUNDS +
            THEMES_DICT[current_theme_image]["image"],
            **kwargs)
        self.current_act_id = ""

    def on_pre_enter(self, *args):
        current_theme_colors = USER_DATA.settings["current_theme_colors"]
        self.primary_color = THEMES_DICT[current_theme_colors]["primary"]
        self.secondary_color = THEMES_DICT[current_theme_colors]["secondary"]
        self.ids.keyboard_layout.build_keyboard()
        return super().on_pre_enter(*args)

    def on_enter(self, *args):
        temp = self.current_act_id.replace("Act", "")
        self.current_level_name = "Act " + temp + " – " + "1"
        self.load_game_play()
        self.load_game_user()
        return super().on_enter(*args)

    def touch_letter(self, letter):
        print(letter)

    def load_game_play(self):
        pass

    def load_game_user(self):
        pass
