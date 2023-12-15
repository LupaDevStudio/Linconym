"""
Module to create the home screen.
"""

###############
### Imports ###
###############

### Kivy imports ###
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.properties import NumericProperty

from tools.path import (
    PATH_BACKGROUNDS
)
from tools.constants import (
    USER_DATA,
    THEMES_DICT,
    GAMEPLAY_DICT
)
from tools.kivy_tools import (
    ImprovedScreen,
)
from screens.custom_widgets import ActButton


#############
### Class ###
#############


class FreeModeScreen(ImprovedScreen):

    def __init__(self, **kwargs) -> None:
        current_background_theme = USER_DATA.settings["current_background_theme"]
        super().__init__(
            back_image_path=PATH_BACKGROUNDS +
            THEMES_DICT[current_background_theme]["image"],
            **kwargs)
        self.fill_scrollview()

    def on_pre_enter(self, *args):
        for act in self.ACT_BUTTON_DICT:
            self.ACT_BUTTON_DICT[act].font_ratio = self.font_ratio
            self.ACT_BUTTON_DICT[act].opacity = 1
        return super().on_pre_enter(*args)

    def on_resize(self, *args):
        for act in self.ACT_BUTTON_DICT:
            self.ACT_BUTTON_DICT[act].font_ratio = self.font_ratio
        return super().on_resize(*args)

    def fill_scrollview(self):
        # Create the layout
        # scrollview_layout = GridLayout(cols=1, row_force_default=True, row_default_height=50,
        #                                pos_hint={'center_x': .5}, size_hint=(None, None))
        # scrollview_layout.bind(minimum_size=scrollview_layout.setter('size'))
        # scrollview_layout.bind(height=scrollview_layout.setter('top'))
        scrollview_layout = self.ids["scrollview_layout"]
        # Load the widgets
        self.ACT_BUTTON_DICT = {}
        for act in GAMEPLAY_DICT:
            act_title = GAMEPLAY_DICT[act]["name"]
            nb_levels = len(GAMEPLAY_DICT[act]) - 1
            if act in USER_DATA.free_mode:
                nb_completed_levels = USER_DATA.free_mode[act]
            else:
                nb_completed_levels = 0
            current_act_button = ActButton(
                act_title=act_title,
                nb_levels=nb_levels,
                nb_completed_levels=nb_completed_levels,
                nb_stars=0,
                font_ratio=self.font_ratio,
                opacity=0)
            self.ACT_BUTTON_DICT[act] = current_act_button
            scrollview_layout.add_widget(self.ACT_BUTTON_DICT[act])
        # self.ids["scrollview"].add_widget(scrollview_layout)
