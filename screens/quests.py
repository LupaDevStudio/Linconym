"""
Module to create the quests screen.
"""

###############
### Imports ###
###############

### Kivy imports ###

from kivy.properties import (
    NumericProperty
)

### Local imports ###

from tools.constants import (
    SCREEN_TUTORIAL,
    SCREEN_BOTTOM_BAR,
    SCREEN_BACK_ARROW,
    SCREEN_TITLE,
    QUESTS_DICT,
    USER_DATA
)
from tools.kivy_tools import (
    LinconymScreen
)
from screens.custom_widgets import (
    QuestsLayout
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
    number_quests = NumericProperty()

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.current_act_id: str
        self.current_level_id: str | None

    def reload_kwargs(self, dict_kwargs):
        self.current_act_id = dict_kwargs["current_act_id"]
        self.current_level_id = dict_kwargs["current_level_id"]
        self.fill_scrollview()

    def fill_scrollview(self):
        scrollview_layout = self.ids["scrollview_layout"]
        # Load the widgets
        self.QUESTS_LAYOUT_DICT = {}
        dict_act_quests = QUESTS_DICT[self.current_act_id]

        if self.current_level_id is not None:
            level_id = self.current_level_id
            if level_id in dict_act_quests:
                for quest_id in dict_act_quests[level_id]:
                    current_quest_layout = self.create_quest_layout(
                        level_id=level_id,
                        quest_id=quest_id
                    )

                    self.QUESTS_LAYOUT_DICT[level_id + quest_id] = current_quest_layout
                    scrollview_layout.add_widget(current_quest_layout)

        else:
            for level_id in dict_act_quests:
                for quest_id in dict_act_quests[level_id]:
                    current_quest_layout = self.create_quest_layout(
                        level_id=level_id,
                        quest_id=quest_id
                    )

                    self.QUESTS_LAYOUT_DICT[level_id + quest_id] = current_quest_layout
                    scrollview_layout.add_widget(current_quest_layout)

    def create_quest_layout(self, level_id: str, quest_id: str):
        self.number_quests += 1

        quest = QUESTS_DICT[self.current_act_id][level_id][quest_id]

        has_completed = False
        has_got_reward = False
        user_data_quests_act = USER_DATA.quests[self.current_act_id]
        if level_id in user_data_quests_act:
            if quest_id in user_data_quests_act[level_id]:
                has_completed = True
                if user_data_quests_act[level_id][quest_id]["has_got_reward"]:
                    has_got_reward = True

        current_quest_layout = QuestsLayout(
            level_id=int(level_id),
            description=quest["quest_content"],
            reward=quest["reward"],
            font_ratio=self.font_ratio,
            primary_color=self.primary_color,
            secondary_color=self.secondary_color)
        current_quest_layout.has_completed = has_completed
        current_quest_layout.has_got_reward = has_got_reward
        
        return current_quest_layout

    def on_leave(self, *args):
        super().on_leave(*args)

        # Reset scrollview
        self.number_quests = 0
        self.ids.scrollview_layout.reset_screen()
