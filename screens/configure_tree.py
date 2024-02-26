"""
Module to create the quests screen.
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

from tools.constants import (
    SCREEN_TUTORIAL,
    SCREEN_BACK_ARROW,
    USER_DATA
)
from tools.kivy_tools import (
    LinconymScreen
)


#############
### Class ###
#############


class ConfigureTreeScreen(LinconymScreen):
    """
    Class to manage the screen that contains the profile information.
    """

    current_level_name = StringProperty()
    dict_type_screen = {
        SCREEN_BACK_ARROW : "",
        SCREEN_TUTORIAL : ""
    }
    dict_type_screen = {
        SCREEN_BACK_ARROW : "",
        SCREEN_TUTORIAL : ""
    }

    nb_stars = NumericProperty()
    start_word = StringProperty("BOY")
    end_word = StringProperty("TOYS")

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.current_act_id: str
        self.current_level_id: str | None

    def reload_kwargs(self, dict_kwargs):
        self.current_act_id = dict_kwargs["current_act_id"]
        self.current_level_id = dict_kwargs["current_level_id"]

    def on_pre_enter(self, *args):
        super().on_pre_enter(*args)

        self.nb_stars = USER_DATA.classic_mode[self.current_act_id][self.current_level_id]["nb_stars"]

        self.ids["tree_layout"].build_layout()

        # Create the title of the screen
        temp = self.current_act_id.replace("Act", "")
        self.current_level_name = "Act " + temp + " – " + self.current_level_id
