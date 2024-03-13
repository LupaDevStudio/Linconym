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
    StringProperty,
    NumericProperty,
    ObjectProperty,
    BooleanProperty,
    BooleanProperty,
    ColorProperty
)

### Local imports ###

from tools.constants import (
    CUSTOM_BUTTON_BACKGROUND_COLOR,
    OPACITY_ON_BUTTON_PRESS
)

#############
### Class ###
#############


class RoundedButtonImage(ButtonBehavior, RelativeLayout):
    """
    A custom button with a white round rectangle background.
    """

    background_color = ColorProperty(CUSTOM_BUTTON_BACKGROUND_COLOR)
    image_path = StringProperty()
    is_icon_color = BooleanProperty(True) # if it's an icon to be colored or not
    colors = ColorProperty((0, 0, 0, 1))
    font_ratio = NumericProperty(1)
    radius = NumericProperty(20)
    release_function = ObjectProperty()
    disable_button = BooleanProperty(False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.always_release = True

    def on_press(self):
        if not self.disable_button:
            self.opacity = OPACITY_ON_BUTTON_PRESS

    def on_release(self):
        if not self.disable_button:
            self.release_function()
            self.opacity = 1
