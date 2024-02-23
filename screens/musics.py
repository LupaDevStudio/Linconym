"""
Module to create the musics screen.
"""

###############
### Imports ###
###############

### Kivy imports ###

from kivy.properties import (
    NumericProperty
)

### Local imports ###

from tools.constants import (
    USER_DATA,
    THEMES_DICT,
    MUSICS_DICT,
    SCREEN_TITLE,
    SCREEN_BACK_ARROW,
    SCREEN_BOTTOM_BAR
)
from tools.kivy_tools import (
    LinconymScreen
)
from screens import (
    MusicLayout
)

#############
### Class ###
#############


class MusicsScreen(LinconymScreen):
    """
    Class to manage the screen that contains the profile information.
    """

    dict_type_screen = {
        SCREEN_TITLE : "Musics",
        SCREEN_BOTTOM_BAR : "none",
        SCREEN_BACK_ARROW : ""
    }

    coins_count = NumericProperty()

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.fill_scrollview()

    def on_pre_enter(self, *args):
        self.coins_count = USER_DATA.user_profile["coins"]
        return super().on_pre_enter(*args)

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
                is_using_music=is_using_music,
                disable_button=True)
            current_music_layout.update_display()
            self.MUSICS_LAYOUT_DICT[music] = current_music_layout
            scrollview_layout.add_widget(current_music_layout)
