"""
Module to create coins counter.
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
    OPACITY_ON_BUTTON_PRESS,
    COINS_COUNT_FONT_SIZE,
)

#############
### Class ###
#############


class SideImageButton(ButtonBehavior, RelativeLayout):
    """
    A custom button with a white round rectangle background.
    """

    background_color = CUSTOM_BUTTON_BACKGROUND_COLOR
    text = StringProperty()
    coins_count = NumericProperty(-1)
    font_size = NumericProperty()
    font_ratio = NumericProperty(1)
    side_image_source = StringProperty()

    def __init__(
            self,
            button_mode=True,
            text_font_name=PATH_TEXT_FONT,
            font_size=COINS_COUNT_FONT_SIZE,
            release_function=lambda: 1 + 1,
            font_ratio=None,
            **kwargs):
        if font_ratio is not None:
            self.font_ratio = font_ratio
        super().__init__(**kwargs)
        self.button_mode = button_mode
        self.release_function = release_function
        self.always_release = True
        self.text_font_name = text_font_name
        self.font_size = font_size

    def on_press(self):
        if self.button_mode:
            self.opacity = OPACITY_ON_BUTTON_PRESS

    def on_release(self):
        if self.button_mode:
            self.release_function()
            self.opacity = 1
