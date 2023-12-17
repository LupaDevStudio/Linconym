"""
Module to create buy and enable buttons
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
    NumericProperty,
    BooleanProperty
)

### Local imports ###

from tools.path import (
    PATH_TEXT_FONT
)
from tools.constants import (
    CUSTOM_BUTTON_BACKGROUND_COLOR,
    OPACITY_ON_BUTTON_PRESS,
    ACT_BUTTON_FONT_SIZE
)

#############
### Class ###
#############


class BuyButton(ButtonBehavior, RelativeLayout):
    """
    A button for the customization screen to buy images or colors.
    """

    background_color = CUSTOM_BUTTON_BACKGROUND_COLOR
    button_title = StringProperty()
    font_size = NumericProperty()
    font_ratio = NumericProperty(1)
    text_font_name = StringProperty(PATH_TEXT_FONT)
    has_bought = BooleanProperty()
    is_using = BooleanProperty()
    price = NumericProperty()

    def __init__(
            self,
            button_title: str = None,
            text_font_name=PATH_TEXT_FONT,
            font_size=ACT_BUTTON_FONT_SIZE,
            has_bought:bool = False,
            is_using: bool = False,
            price: int = 0,
            release_function=lambda: 1 + 1,
            font_ratio=None,
            **kwargs):

        if button_title is not None:
            self.button_title = button_title
        if font_ratio is not None:
            self.font_ratio = font_ratio

        self.release_function = release_function
        self.has_bought = has_bought
        self.is_using = is_using
        self.price = price

        super().__init__(**kwargs)
        self.text_font_name = text_font_name
        self.font_size = font_size

    def on_press(self):
        self.opacity = OPACITY_ON_BUTTON_PRESS

    def on_release(self):
        self.release_function()
        self.opacity = 1

