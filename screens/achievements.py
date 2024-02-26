"""
Module to create the quests screen.
"""

###############
### Imports ###
###############

### Python imports ###

from typing import Literal

### Kivy imports ###

from kivy.properties import (
    StringProperty
)

### Local imports ###

from tools.constants import (
    SCREEN_TUTORIAL,
    SCREEN_BOTTOM_BAR,
    SCREEN_BACK_ARROW,
    SCREEN_TITLE
)
from tools.kivy_tools import (
    LinconymScreen
)


#############
### Class ###
#############


class AchievementsScreen(LinconymScreen):
    """
    Class to manage the screen that contains the achievements.
    """

    dict_type_screen = {
        SCREEN_TITLE : "Achievements",
        SCREEN_BOTTOM_BAR : "none",
        SCREEN_BACK_ARROW : "",
        SCREEN_TUTORIAL : ""
    }
    mode : Literal["classic", "daily"] = StringProperty() 
