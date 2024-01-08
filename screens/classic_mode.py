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

    def on_enter(self, *args):
        current_theme_image = USER_DATA.settings["current_theme_image"]
        current_theme_colors = USER_DATA.settings["current_theme_colors"]
        self.primary_color = THEMES_DICT[current_theme_colors]["primary"]
        self.secondary_color = THEMES_DICT[current_theme_colors]["secondary"]
        self.set_back_image_path(
            PATH_BACKGROUNDS + THEMES_DICT[current_theme_image]["image"])
        return super().on_enter(*args)

    def on_resize(self, *args):
        for act in self.ACT_BUTTON_DICT:
            self.ACT_BUTTON_DICT[act].font_ratio = self.font_ratio
        return super().on_resize(*args)

    def go_backwards(self):
        self.manager.current = "home"

    def fill_scrollview(self):
        scrollview_layout = self.ids["scrollview_layout"]
        # Load the widgets
        self.ACT_BUTTON_DICT = {}
        for act in GAMEPLAY_DICT:
            act_title = GAMEPLAY_DICT[act]["name"]
            nb_levels = len(GAMEPLAY_DICT[act]) - 1
            if act in USER_DATA.classic_mode:
                nb_completed_levels = USER_DATA.classic_mode[act]
            else:
                nb_completed_levels = 0
            current_act_button = ActButton(
                act_title=act_title,
                nb_levels=nb_levels,
                nb_completed_levels=nb_completed_levels,
                nb_stars=0,
                font_ratio=self.font_ratio,
                release_function=partial(self.open_levels_screen, act))
            self.ACT_BUTTON_DICT[act] = current_act_button
            scrollview_layout.add_widget(self.ACT_BUTTON_DICT[act])

    def open_levels_screen(self, act_id):
        self.manager.get_screen("levels").current_act_id = act_id
        self.manager.current = "levels"
