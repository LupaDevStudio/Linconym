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
    BooleanProperty,
    ColorProperty
)

### Local imports ###

from tools.path import (
    PATH_TEXT_FONT
)

#############
### Class ###
#############


class ColoredRoundedButtonImage(ButtonBehavior, RelativeLayout):
    """
    A custom button with a colored round rectangle background and an image in it.
    """

    background_color = ColorProperty()
    touch_color = ColorProperty()
    image_path = StringProperty()
    text_filling_ratio = NumericProperty()
    font_size = NumericProperty()
    font_ratio = NumericProperty(1)
    disable_button = BooleanProperty(False)
    color_image = ColorProperty()
    text_font_name = StringProperty(PATH_TEXT_FONT)

    def __init__(
            self,
            release_function=lambda: 1 + 1,
            font_ratio=None,
            **kwargs):
        if font_ratio is not None:
            self.font_ratio = font_ratio
        super().__init__(**kwargs)
        self.release_function = release_function
        self.always_release = True

        self.bind(disable_button=self.bind_function)
        self.bind(color_image=self.bind_function)
        self.bind(background_color=self.bind_function)
        self.bind(touch_color=self.bind_function)
        self.bind(image_path=self.bind_function)

    def bind_function(self, base_widget, value):
        pass

    def on_press(self):
        if not self.disable_button:
            self.temp_color = self.background_color
            self.background_color = self.touch_color

    def on_release(self):
        if not self.disable_button:
            self.release_function()
            self.background_color = self.temp_color
