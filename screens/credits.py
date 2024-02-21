"""
Module to create the profile screen.
"""

###############
### Imports ###
###############

### Python imports ###

from functools import partial

### Kivy imports ###

from kivy.properties import (
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
    MUSICS_DICT
)
from tools.kivy_tools import (
    ImprovedScreen
)
from screens import (
    MusicLayout
)


#############
### Class ###
#############


class CreditsScreen(ImprovedScreen):
    """
    Class to display the credits of the application.
    """

    primary_color = ColorProperty((0, 0, 0, 1))
    secondary_color = ColorProperty((0, 0, 0, 1))
    number_lines_credits = NumericProperty()

    def __init__(self, **kwargs) -> None:
        current_theme_image = USER_DATA.settings["current_theme_image"]
        super().__init__(
            back_image_path=PATH_BACKGROUNDS +
            THEMES_DICT[current_theme_image]["image"],
            **kwargs)
        self.fill_scrollview()

    def on_enter(self, *args):
        current_theme_image = USER_DATA.settings["current_theme_image"]
        current_theme_colors = USER_DATA.settings["current_theme_colors"]
        self.primary_color = THEMES_DICT[current_theme_colors]["primary"]
        self.secondary_color = THEMES_DICT[current_theme_colors]["secondary"]
        self.set_back_image_path(
            PATH_BACKGROUNDS + THEMES_DICT[current_theme_image]["image"])
        return super().on_enter(*args)

    def fill_scrollview(self):
        # Load the widgets
        self.number_lines_credits = 0
        current_theme_colors = USER_DATA.settings["current_theme_colors"]
        scrollview_layout = self.ids["scrollview_layout"]

        self.CREDITS_LAYOUT_DICT = {}

        # Add the musics
        for music in MUSICS_DICT:
            self.number_lines_credits += 1
            music_credit_layout = MusicLayout(
                music_key=music,
                font_ratio=self.font_ratio * 0.8,
                primary_color=THEMES_DICT[current_theme_colors]["primary"],
                radius=20)
            music_credit_layout.disable_buy_select()
            music_credit_layout.release_function = partial(
                self.open_url, MUSICS_DICT[music]["license"])
            self.CREDITS_LAYOUT_DICT[music] = music_credit_layout
            scrollview_layout.add_widget(music_credit_layout)

    def open_url(self, url):
        print(url)
