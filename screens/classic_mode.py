"""
Module to create the home screen.
"""

###############
### Imports ###
###############

### Python imports ###

from functools import partial

### Kivy imports ###

from kivy.properties import (
    ColorProperty
)

### Local imports ###

from tools.path import (
    PATH_BACKGROUNDS
)
from tools.constants import (
    USER_DATA,
    THEMES_DICT,
    GAMEPLAY_DICT
)
from tools.kivy_tools import (
    ImprovedScreen
)
from screens.custom_widgets import (
    ActButton
)

#############
### Class ###
#############


class ClassicModeScreen(ImprovedScreen):

    primary_color = ColorProperty((0, 0, 0, 1))
    secondary_color = ColorProperty((0, 0, 0, 1))

    def __init__(self, **kwargs) -> None:
        current_theme_image = USER_DATA.settings["current_theme_image"]
        super().__init__(
            back_image_path=PATH_BACKGROUNDS +
            THEMES_DICT[current_theme_image]["image"],
            **kwargs)
        self.ACT_BUTTON_DICT = {}
        self.on_resize()
        self.fill_scrollview()

    def on_pre_enter(self, *args):
        current_theme_image = USER_DATA.settings["current_theme_image"]
        current_theme_colors = USER_DATA.settings["current_theme_colors"]
        self.primary_color = THEMES_DICT[current_theme_colors]["primary"]
        self.secondary_color = THEMES_DICT[current_theme_colors]["secondary"]
        self.set_back_image_path(
            PATH_BACKGROUNDS + THEMES_DICT[current_theme_image]["image"])
        for act in self.ACT_BUTTON_DICT:
            self.ACT_BUTTON_DICT[act].primary_color = self.primary_color
            self.ACT_BUTTON_DICT[act].secondary_color = self.secondary_color
        return super().on_pre_enter(*args)

    def on_resize(self, *args):
        for act in self.ACT_BUTTON_DICT:
            self.ACT_BUTTON_DICT[act].font_ratio = self.font_ratio
        return super().on_resize(*args)

    def fill_scrollview(self):
        scrollview_layout = self.ids["scrollview_layout"]
        # Load the widgets
        self.ACT_BUTTON_DICT = {}
        for act in GAMEPLAY_DICT:
            act_title = GAMEPLAY_DICT[act]["name"]
            nb_levels = len(GAMEPLAY_DICT[act]) - 1
            if act in USER_DATA.classic_mode:
                nb_completed_levels = len(USER_DATA.classic_mode[act])
            else:
                nb_completed_levels = 0
            current_act_button = ActButton(
                act_title=act_title,
                nb_levels=nb_levels,
                nb_completed_levels=nb_completed_levels,
                nb_stars=2,
                font_ratio=self.font_ratio,
                release_function=partial(self.open_levels_screen, act),
                primary_color=self.primary_color,
                secondary_color=self.secondary_color)
            self.ACT_BUTTON_DICT[act] = current_act_button
            scrollview_layout.add_widget(self.ACT_BUTTON_DICT[act])

    def open_levels_screen(self, act_id):
        dict_kwargs = {
                "current_act_id": act_id
            }
        self.manager.go_to_next_screen(
            next_screen_name="levels",
            next_dict_kwargs=dict_kwargs)
