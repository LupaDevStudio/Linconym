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
        current_theme_image = USER_DATA.settings["current_theme_image"]
        super().__init__(
            back_image_path=PATH_BACKGROUNDS +
            THEMES_DICT[current_theme_image]["image"],
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
            image_price = THEMES_DICT[theme]["image_price"]
            primary_color = THEMES_DICT[theme]["primary"]
            secondary_color = THEMES_DICT[theme]["secondary"]
            if theme in USER_DATA.unlocked_themes:
                has_bought_image = USER_DATA.unlocked_themes[theme]["image"]
                has_bought_colors = USER_DATA.unlocked_themes[theme]["colors"]
                if USER_DATA.settings["current_theme_image"] == theme:
                    is_using_image = True
                else:
                    is_using_image = False
                if USER_DATA.settings["current_theme_colors"] == theme:
                    is_using_colors = True
                else:
                    is_using_colors = False
            else:
                has_bought_image = False
                has_bought_colors = False
                is_using_image = False
                is_using_colors = False
            current_theme_button = ThemeLayout(
                theme_title=theme_title,
                source=PATH_BACKGROUNDS + THEMES_DICT[theme]["image"],
                font_ratio=self.font_ratio * 0.8,
                image_price=image_price,
                has_bought_image=has_bought_image,
                is_using_image=is_using_image,
                has_bought_colors=has_bought_colors,
                is_using_colors=is_using_colors,
                primary_color=primary_color,
                secondary_color=secondary_color)
            current_theme_button.update_display()
            self.THEME_LAYOUT_DICT[theme] = current_theme_button
            scrollview_layout.add_widget(self.THEME_LAYOUT_DICT[theme])
