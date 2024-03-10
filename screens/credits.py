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
    CREDITS_DICT,
    SCREEN_TITLE,
    SCREEN_BACK_ARROW,
    SCREEN_BOTTOM_BAR,
    SMALL_LABEL_FONT_SIZE
)
from screens.custom_widgets import (
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
        SCREEN_TITLE: "Credits",
        SCREEN_BACK_ARROW: "",
        SCREEN_BOTTOM_BAR: "none"
    }
    number_lines_credits = NumericProperty()

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.fill_scrollview()

    def fill_scrollview(self):
        # Load the widgets
        self.number_lines_credits = 0
        scrollview_layout = self.ids["scrollview_layout"]

        self.CREDITS_LAYOUT_DICT = {}

        # Add the musics
        musics_dict = CREDITS_DICT["musics"]
        for music in musics_dict:
            self.number_lines_credits += 1
            title = musics_dict[music]["name"] + \
                " – " + musics_dict[music]["author"]
            music_credit_layout = MusicLayout(
                music_title=title,
                font_ratio=self.font_ratio * 0.8,
                primary_color=self.primary_color,
                radius=20,
                font_size=SMALL_LABEL_FONT_SIZE)
            music_credit_layout.disable_buy_select()
            music_credit_layout.release_function = partial(
                self.open_url, musics_dict[music]["license"])
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
