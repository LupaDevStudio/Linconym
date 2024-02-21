"""
Module to create the preview screen.
"""

###############
### Imports ###
###############

### Kivy imports ###

from kivy.properties import (
    StringProperty,
    ColorProperty,
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


#############
### Class ###
#############


class PreviewScreen(ImprovedScreen):
    """
    Class to manage the screen that contains the profile information.
    """

    primary_color = ColorProperty((0, 0, 0, 1))
    secondary_color = ColorProperty((0, 0, 0, 1))
    theme_key = StringProperty()
    coins_count = NumericProperty()

    def __init__(self, **kwargs) -> None:
        # TODO : to change with the theme_key
        current_theme_image = USER_DATA.settings["current_theme_image"]
        super().__init__(
            back_image_path=PATH_BACKGROUNDS +
            THEMES_DICT[current_theme_image]["image"],
            **kwargs)

    def reload_kwargs(self, dict_kwargs):
        if "theme_key" in dict_kwargs:
            self.theme_key = dict_kwargs["theme_key"]

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
