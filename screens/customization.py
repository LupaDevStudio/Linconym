"""
Module to create the customization screen.
"""

###############
### Imports ###
###############

from tools.path import (
    PATH_BACKGROUNDS
)
from tools.constants import (
    USER_DATA,
    THEMES_DICT
)
from tools.kivy_tools import (
    ImprovedScreen,
)
from screens.custom_widgets import ThemeLayout


#############
### Class ###
#############


class CustomizationScreen(ImprovedScreen):
    """
    Class to manage the customization screen.
    """

    def __init__(self, **kwargs) -> None:
        current_background_theme = USER_DATA.settings["current_background_theme"]
        super().__init__(
            back_image_path=PATH_BACKGROUNDS +
            THEMES_DICT[current_background_theme]["image"],
            **kwargs)
        self.THEME_LAYOUT_DICT = {}
        self.on_resize()
        self.fill_scrollview()

    def on_resize(self, *args):
        for act in self.THEME_LAYOUT_DICT:
            self.THEME_LAYOUT_DICT[act].font_ratio = self.font_ratio
        return super().on_resize(*args)

    def fill_scrollview(self):
        scrollview_layout = self.ids["scrollview_layout"]
        # Load the widgets
        self.THEME_LAYOUT_DICT = {}
        for theme in THEMES_DICT:
            theme_title = THEMES_DICT[theme]["name"]
            current_act_button = ThemeLayout(
                theme_title=theme_title,
                source=PATH_BACKGROUNDS + THEMES_DICT[theme]["image"],
                font_ratio=self.font_ratio*0.8)
            self.THEME_LAYOUT_DICT[theme] = current_act_button
            scrollview_layout.add_widget(self.THEME_LAYOUT_DICT[theme])
