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

### Local imports ###

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
    value = NumericProperty()

    def __init__(
            self,
            value=0,
            **kwargs):
        super().__init__(**kwargs)
        self.value = value

    def on_kv_post(self, base_widget):
        self.ids.my_slider.bind(value=self.on_value_change)
        return super().on_kv_post(base_widget)

    def on_value_change(self, base_widget, value):
        self.value = value
