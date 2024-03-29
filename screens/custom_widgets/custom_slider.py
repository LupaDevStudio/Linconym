"""
Module to create custom buttons with round transparent white background.
"""

###############
### Imports ###
###############


### Kivy imports ###

from kivy.uix.slider import Slider
from kivy.properties import (
    NumericProperty,
    ColorProperty
)

### Local imports ###

from tools.constants import (
    CUSTOM_BUTTON_BACKGROUND_COLOR
)


#############
### Class ###
#############


class CustomSlider(Slider):
    """
    A custom slider.
    """

    primary_color = ColorProperty((0, 0, 0, 1))
    secondary_color = ColorProperty((1, 1, 1, 1))

    font_ratio = NumericProperty(1)

    def __init__(
            self,
            **kwargs):
        super().__init__(**kwargs)
        self.cursor_width = 0
        self.cursor_height = 0
        self.border_horizontal = [0, 0, 0, 0]

    # def func(self):
    #     pass
