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
    SCREEN_TITLE,
    ACHIEVEMENTS_DICT,
    USER_DATA
)
from screens.custom_widgets import (
    AchievementsLayout
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


    def on_pre_enter(self, *args):
        super().on_pre_enter(*args)
        self.fill_scrollview()

    def fill_scrollview(self):
        scrollview_layout = self.ids.scrollview_layout

        # Load the widgets
        self.ACHIEVEMENTS_LAYOUT_DICT = {}

        for achievement_id in ACHIEVEMENTS_DICT:
            achievement = ACHIEVEMENTS_DICT[achievement_id]

            # Get the data of the user
            has_completed = False
            has_got_reward = False
            if achievement_id in USER_DATA.achievements:
                has_completed = True
                if USER_DATA.achievements[achievement_id]:
                    has_got_reward = True

            current_achievement_layout = AchievementsLayout(
                achievement_title=achievement["achievement_title"],
                description=achievement["achievement_content"],
                reward=achievement["reward"],
                font_ratio=self.font_ratio,
                primary_color=self.primary_color,
                secondary_color=self.secondary_color,
                size_hint=(0.8, None),
                height=150*self.font_ratio)
            current_achievement_layout.has_completed = has_completed
            current_achievement_layout.has_got_reward = has_got_reward

            self.ACHIEVEMENTS_LAYOUT_DICT[achievement_id] = current_achievement_layout
            scrollview_layout.add_widget(current_achievement_layout)

    def on_leave(self, *args):
        super().on_leave(*args)

        # Reset scrollview
        self.ids.scrollview_layout.reset_scrollview()
