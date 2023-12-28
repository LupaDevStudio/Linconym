"""
Module to create coins counter.
"""

###############
### Imports ###
###############

### Kivy imports ###
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import (
    StringProperty,
    NumericProperty,
    ColorProperty
)

### Local imports ###
from tools.path import (
    PATH_TEXT_FONT
)
from tools.constants import (
    CUSTOM_BUTTON_BACKGROUND_COLOR,
    OPACITY_ON_BUTTON_PRESS,
    EXPERIENCE_FONT_SIZE,
    THEMES_DICT
)

#############
### Class ###
#############


class ExperienceCounter(RelativeLayout):
    """
    A custom layout for the experience counter.
    """

    background_color = CUSTOM_BUTTON_BACKGROUND_COLOR
    label_experience_left = StringProperty()
    percentage_experience = NumericProperty()
    experience_left = NumericProperty()
    font_size = NumericProperty()
    font_ratio = NumericProperty(1)
    theme_colors = StringProperty()
    primary_color = ColorProperty()
    secondary_color = ColorProperty()

    def __init__(
            self,
            text_font_name=PATH_TEXT_FONT,
            font_size=EXPERIENCE_FONT_SIZE,
            font_ratio=None,
            **kwargs):
        if font_ratio is not None:
            self.font_ratio = font_ratio
        super().__init__(**kwargs)
        self.bind(percentage_experience=self.update_experience)
        self.bind(experience_left=self.update_experience)
        self.bind(theme_colors=self.update_colors)
        self.text_font_name = text_font_name
        self.font_size = font_size

    def update_colors(self, base_widget, value):
        self.primary_color = THEMES_DICT[self.theme_colors]["primary"]
        self.secondary_color = THEMES_DICT[self.theme_colors]["secondary"]

    def update_experience(self, base_widget, value):
        self.label_experience_left = "+ " + str(self.experience_left) + " XP"

    def on_press(self):
        if self.button_mode:
            self.opacity = OPACITY_ON_BUTTON_PRESS

    def on_release(self):
        if self.button_mode:
            self.release_function()
            self.opacity = 1
