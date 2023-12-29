"""
Module to create custom buttons with round transparent white background.
"""

###############
### Imports ###
###############

### Kivy imports ###
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import (
    BooleanProperty
)

### Local imports ###

from tools.constants import (
    OPACITY_ON_BUTTON_PRESS
)

#############
### Class ###
#############


class CircleIconButton(ButtonBehavior, Image):
    """
    A custom button with a white round rectangle background.
    """

    disable_button = BooleanProperty()

    def __init__(
            self,
            release_function=lambda: 1 + 1,
            **kwargs):
        super().__init__(**kwargs)
        self.always_release = True
        self.release_function = release_function
        self.bind(disable_button=self.bind_function)

    def bind_function(self, base_widget, value):
        pass

    def on_press(self):
        if not self.disable_button:
            self.opacity = OPACITY_ON_BUTTON_PRESS

    def on_release(self):
        if not self.disable_button:
            self.release_function()
            self.opacity = 1

