"""
Module to create custom buttons with round transparent white background.
"""

###############
### Imports ###
###############

### Kivy imports ###

from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import (
    NumericProperty
)

### Module imports ###

from tools.constants import (
    CUSTOM_BUTTON_BACKGROUND_COLOR
)

#############
### Class ###
#############


class CustomSlider(RelativeLayout):
    """
    A custom slider.
    """

    background_color = CUSTOM_BUTTON_BACKGROUND_COLOR
    slider_value = NumericProperty()

    def __init__(
            self,
            on_value_change=None,
            slider_value=0,
            **kwargs):
        super().__init__(**kwargs)
        self.slider_value = slider_value
        if not on_value_change is None:
            self.ids.my_slider.bind(value=on_value_change)
