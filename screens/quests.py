"""
Module to create the quests screen.
"""

###############
### Imports ###
###############

### Kivy imports ###

from kivy.properties import (
    StringProperty,
    ColorProperty
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


class QuestsScreen(ImprovedScreen):
    """
    Class to manage the screen that contains the profile information.
    """

    primary_color = ColorProperty((0, 0, 0, 1))
    secondary_color = ColorProperty((0, 0, 0, 1))

    def __init__(self, **kwargs) -> None:
        current_theme_image = USER_DATA.settings["current_theme_image"]
        super().__init__(
            back_image_path=PATH_BACKGROUNDS +
            THEMES_DICT[current_theme_image]["image"],
            **kwargs)
        self.current_act_id: str
        self.current_level_id: str | None

    def reload_kwargs(self, dict_kwargs):
        self.current_act_id = dict_kwargs["current_act_id"]
        self.current_level_id = dict_kwargs["current_level_id"]

    def on_enter(self, *args):
        current_theme_image = USER_DATA.settings["current_theme_image"]
        current_theme_colors = USER_DATA.settings["current_theme_colors"]
        self.primary_color = THEMES_DICT[current_theme_colors]["primary"]
        self.secondary_color = THEMES_DICT[current_theme_colors]["secondary"]
        self.set_back_image_path(
            PATH_BACKGROUNDS + THEMES_DICT[current_theme_image]["image"])
        return super().on_enter(*args)
