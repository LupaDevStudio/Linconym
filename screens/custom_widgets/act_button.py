"""
Module to create the act button.
"""

###############
### Imports ###
###############

### Python imports ###
from typing import Literal

### Kivy imports ###
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import (
    StringProperty,
    NumericProperty
)

### Local imports ###
from tools.path import (
    PATH_TEXT_FONT
)
from tools.constants import (
    CUSTOM_BUTTON_BACKGROUND_COLOR,
    MAIN_BUTTON_FONT_SIZE,
    OPACITY_ON_BUTTON_PRESS
)

#############
### Class ###
#############


class ActButton(ButtonBehavior, RelativeLayout):
    """
    A custom button with a white round rectangle background.
    """

    background_color = CUSTOM_BUTTON_BACKGROUND_COLOR
    act_title = StringProperty()
    completion_text = StringProperty()
    font_size = NumericProperty()
    font_ratio = NumericProperty(1)
    nb_levels = NumericProperty()
    nb_completed_levels = NumericProperty()
    nb_stars = NumericProperty()
    text_font_name = StringProperty(PATH_TEXT_FONT)

    def __init__(
            self,
            act_title: str = None,
            nb_levels: int = None,
            nb_completed_levels: int = None,
            nb_stars: Literal[0, 1, 2, 3] = None,
            parent=None,
            text_font_name=PATH_TEXT_FONT,
            font_size=MAIN_BUTTON_FONT_SIZE,
            release_function=lambda: 1 + 1,
            font_ratio=None,
            **kwargs):

        if act_title is not None:
            self.act_title = act_title
        if nb_levels is not None:
            self.nb_levels = nb_levels
        if nb_completed_levels is not None:
            self.nb_completed_levels = nb_completed_levels
        if nb_stars is not None:
            self.nb_stars = nb_stars
        if parent is not None:
            self.parent = parent
        if font_ratio is not None:
            self.font_ratio = font_ratio

        super().__init__(**kwargs)
        self.release_function = release_function
        self.always_release = True
        self.text_font_name = text_font_name
        self.font_size = font_size
        self.bind(nb_completed_levels=self.update_nb_completed_levels)
        self.update_nb_completed_levels(None, None)

    def update_nb_completed_levels(self, base_widget, value):
        self.completion_text = str(
            self.nb_completed_levels) + "/" + str(self.nb_levels)

    def on_press(self):
        self.opacity = OPACITY_ON_BUTTON_PRESS

    def on_release(self):
        self.release_function()
        self.opacity = 1
