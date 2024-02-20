"""
Module to create the act button.
"""

###############
### Imports ###
###############

### Python imports ###

from typing import Literal

### Kivy imports ###

from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import (
    StringProperty,
    NumericProperty,
    ColorProperty,
    BooleanProperty
)

### Local imports ###

from tools.path import (
    PATH_TEXT_FONT
)
from tools.constants import (
    CUSTOM_BUTTON_BACKGROUND_COLOR,
    MUSICS_DICT,
    LABEL_FONT_SIZE
)

#############
### Class ###
#############


class MusicLayout(RelativeLayout):
    """
    A custom button with a white round rectangle background.
    """

    background_color = CUSTOM_BUTTON_BACKGROUND_COLOR
    music_title = StringProperty()
    font_size = NumericProperty(LABEL_FONT_SIZE)
    font_ratio = NumericProperty(1)
    text_font_name = StringProperty(PATH_TEXT_FONT)
    primary_color = ColorProperty((1, 1, 1, 1))
    radius = NumericProperty(40)
    music_key = StringProperty()
    is_playing = BooleanProperty(False)

    def __init__(
            self,
            music_key: str = "",
            release_function=lambda: 1 + 1,
            font_ratio=None,
            **kwargs):

        if font_ratio is not None:
            self.font_ratio = font_ratio

        super().__init__(**kwargs)
        self.release_function = release_function
        self.always_release = True
        self.music_title = MUSICS_DICT[music_key]["name"]

    def play_sound(self):
        if self.is_playing:
            # TODO play the former music
            self.is_playing = False
        else:
            # TODO play the new music
            self.is_playing = True
