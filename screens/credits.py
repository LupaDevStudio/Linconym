"""
Module to create the profile screen.
"""

###############
### Imports ###
###############

### Python imports ###

from functools import partial
import webbrowser

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


class CreditsScreen(LinconymScreen):
    """
    Class to display the credits of the application.
    """

    dict_type_screen = {
        SCREEN_TITLE : "Credits",
        SCREEN_BACK_ARROW : "",
        SCREEN_BOTTOM_BAR : "none"
    }
    number_lines_credits = NumericProperty()

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.fill_scrollview()

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
        """
        Open the url given as argument.

        Parameters
        ----------
        url : str
            Url of the credit item.

        Returns
        -------
        None
        """
        webbrowser.open(url, 2)
