"""
Module to create the settings screen.
"""

###############
### Imports ###
###############

### Kivy imports ###

from kivy.properties import StringProperty

### Module imports ###

from tools.constants import (
    USER_DATA,
    THEMES_DICT,
    __version__
)
from tools.kivy_tools import (
    ImprovedScreen,
)
from tools.path import (
    PATH_BACKGROUNDS
)

#############
### Class ###
#############


class SettingsScreen(ImprovedScreen):
    """
    Class to manage the settings screen.
    """

    version_text = StringProperty()

    def __init__(self, **kwargs) -> None:
        current_background_theme = USER_DATA.settings["current_background_theme"]
        self.version_text = "Version " + str(__version__)
        super().__init__(
            back_image_path=PATH_BACKGROUNDS +
            THEMES_DICT[current_background_theme]["image"],
            **kwargs)
