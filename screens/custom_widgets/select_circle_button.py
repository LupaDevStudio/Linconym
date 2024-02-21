"""
Module to create buy and enable buttons
"""


###############
### Imports ###
###############

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


class SelectCircleButton(ButtonBehavior, RelativeLayout):
    """
    A button for the customization screen to buy images or colors.
    """

    font_ratio = NumericProperty(1)
    is_using = BooleanProperty(False)
    disable_button = BooleanProperty(False)

    def __init__(
            self,
            release_function=lambda: 1 + 1,
            font_ratio=None,
            **kwargs):

        if font_ratio is not None:
            self.font_ratio = font_ratio

        self.release_function = release_function
        self.always_release = True

        super().__init__(**kwargs)

    def on_press(self):
        if not self.disable_button:
            self.opacity = OPACITY_ON_BUTTON_PRESS

    def on_release(self):
        if not self.disable_button:
            self.release_function()
            self.opacity = 1
