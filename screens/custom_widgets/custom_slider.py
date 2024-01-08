"""
Module to create custom buttons with round transparent white background.
"""

###############
### Imports ###
###############

### Python imports ###

import shutil

### Kivy imports ###

from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import (
    NumericProperty
)
from kivy.clock import Clock

### Local imports ###

from tools.constants import (
    CUSTOM_BUTTON_BACKGROUND_COLOR
)

from tools.path import (
    PATH_TEMP_IMAGES
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
        self.update_textures()
        return super().on_kv_post(base_widget)

    def on_value_change(self, base_widget, value):
        self.value = value

    def set_textures(self, *args):
        self.ids["my_slider"].cursor_image = PATH_TEMP_IMAGES + \
            "spinner_circle_texture.png"
        self.ids["my_slider"].background_horizontal = PATH_TEMP_IMAGES + \
            "customization.png"

    def update_textures(self, save_int=0):
        self.ids["my_slider"].cursor_image = PATH_TEMP_IMAGES + \
            f"circle_{save_int}.png"
        self.ids["my_slider"].background_horizontal = PATH_TEMP_IMAGES + \
            f"rectangle_{save_int}.png"
