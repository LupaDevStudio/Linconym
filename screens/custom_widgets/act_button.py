"""
Module to create the act button.
"""

###############
### Imports ###
###############

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
    nb_levels = NumericProperty()
    nb_completed_levels = NumericProperty()
    stars_number = NumericProperty()

    def __init__(
            self,
            text_font_name=PATH_TEXT_FONT,
            font_size=MAIN_BUTTON_FONT_SIZE,
            release_function=lambda: 1 + 1,
            **kwargs):
        super().__init__(**kwargs)
        self.release_function = release_function
        self.always_release = True
        self.text_font_name = text_font_name
        self.font_size = font_size
        self.bind(nb_completed_levels=self.update_nb_completed_levels)

    def update_nb_completed_levels(self, base_widget, value):
        self.completion_text = str(
            self.nb_completed_levels) + "/" + str(self.nb_levels)

    def on_press(self):
        self.opacity = OPACITY_ON_BUTTON_PRESS

    def on_release(self):
        self.release_function()
        self.opacity = 1
