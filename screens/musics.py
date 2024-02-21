"""
Module to create the musics screen.
"""

###############
### Imports ###
###############

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


class MusicsScreen(ImprovedScreen):
    """
    Class to manage the screen that contains the profile information.
    """

    coins_count = NumericProperty()
    primary_color = ColorProperty((0, 0, 0, 1))
    secondary_color = ColorProperty((0, 0, 0, 1))

    def __init__(self, **kwargs) -> None:
        current_theme_image = USER_DATA.settings["current_theme_image"]
        super().__init__(
            back_image_path=PATH_BACKGROUNDS +
            THEMES_DICT[current_theme_image]["image"],
            **kwargs)
        self.fill_scrollview()

    def on_enter(self, *args):
        self.coins_count = USER_DATA.user_profile["coins"]
        current_theme_image = USER_DATA.settings["current_theme_image"]
        current_theme_colors = USER_DATA.settings["current_theme_colors"]
        self.primary_color = THEMES_DICT[current_theme_colors]["primary"]
        self.secondary_color = THEMES_DICT[current_theme_colors]["secondary"]
        self.set_back_image_path(
            PATH_BACKGROUNDS + THEMES_DICT[current_theme_image]["image"])
        return super().on_enter(*args)

    def go_to_boosters(self):
        self.go_to_next_screen(screen_name="boosters")

    def fill_scrollview(self):
        scrollview_layout = self.ids["scrollview_layout"]
        # Load the widgets
        self.MUSICS_LAYOUT_DICT = {}
        current_theme_colors = USER_DATA.settings["current_theme_colors"]
        for music in MUSICS_DICT:
            has_bought_music = USER_DATA.unlocked_musics[music]
            is_using_music = USER_DATA.settings["current_music"] == music
            current_music_layout = MusicLayout(
                music_key=music,
                font_ratio=self.font_ratio * 0.8,
                primary_color=THEMES_DICT[current_theme_colors]["primary"],
                has_bought_music=has_bought_music,
                is_using_music=is_using_music)
            current_music_layout.update_display()
            self.MUSICS_LAYOUT_DICT[music] = current_music_layout
            scrollview_layout.add_widget(self.MUSICS_LAYOUT_DICT[music])
