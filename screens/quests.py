"""
Module to create the quests screen.
"""

###############
### Imports ###
###############

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


class QuestsScreen(LinconymScreen):
    """
    Class to manage the screen that contains the profile information.
    """

    dict_type_screen = {
        SCREEN_TITLE : "Quests",
        SCREEN_BOTTOM_BAR : "none",
        SCREEN_BACK_ARROW : "",
        SCREEN_TUTORIAL : ""
    }

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.current_act_id: str
        self.current_level_id: str | None

    def reload_kwargs(self, dict_kwargs):
        self.current_act_id = dict_kwargs["current_act_id"]
        self.current_level_id = dict_kwargs["current_level_id"]
