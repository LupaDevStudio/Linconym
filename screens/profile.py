"""
Module to create the profile screen.
"""

###############
### Imports ###
###############

### Kivy imports ###

from kivy.properties import (
    StringProperty,
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


class ProfileScreen(ImprovedScreen):
    """
    Class to manage the screen that contains the profile information.
    """

    user_status = StringProperty()
    user_level = StringProperty()
    coins_count = NumericProperty()
    theme_colors = StringProperty()

    def __init__(self, **kwargs) -> None:
        current_theme_image = USER_DATA.settings["current_theme_image"]
        super().__init__(
            back_image_path=PATH_BACKGROUNDS +
            THEMES_DICT[current_theme_image]["image"],
            **kwargs)

    def on_enter(self, *args):
        self.coins_count = USER_DATA.user_profile["coins"]
        self.user_level = "Level " + str(USER_DATA.user_profile["level"])
        current_theme_image = USER_DATA.settings["current_theme_image"]
        self.theme_colors = USER_DATA.settings["current_theme_colors"]
        self.user_status = USER_DATA.user_profile["status"]
        self.set_back_image_path(
            PATH_BACKGROUNDS + THEMES_DICT[current_theme_image]["image"])
        return super().on_enter(*args)
