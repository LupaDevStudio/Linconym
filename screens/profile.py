"""
Module to create the profile screen.
"""

###############
### Imports ###
###############

### Kivy imports ###

from kivy.properties import StringProperty

### Module imports ###

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

    def __init__(self, **kwargs) -> None:
        current_background_theme = USER_DATA.settings["current_background_theme"]
        super().__init__(
            back_image_path=PATH_BACKGROUNDS +
            THEMES_DICT[current_background_theme]["image"],
            **kwargs)
        
        self.user_status = USER_DATA.user_profile["status"]
        self.user_level = "Level " + str(USER_DATA.user_profile["level"])
