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
    NumericProperty
)

### Local imports ###
from tools.path import (
    PATH_TEXT_FONT
)
from tools.constants import (
    CUSTOM_BUTTON_BACKGROUND_COLOR,
    MAIN_BUTTON_FONT_SIZE,
    OPACITY_ON_BUTTON_PRESS,
    CONTENT_LABEL_FONT_SIZE
)

#############
### Class ###
#############


class CustomContentLabel(ButtonBehavior, RelativeLayout):
    """
    A custom button with a white round rectangle background.
    """

    background_color = CUSTOM_BUTTON_BACKGROUND_COLOR
    title = StringProperty()
    content = StringProperty()
    text_filling_ratio = NumericProperty()
    font_size_title = NumericProperty()
    font_size_content = NumericProperty()
    font_ratio = NumericProperty()

    def __init__(
            self,
            title="",
            content="",
            button_mode=True,
            text_font_name=PATH_TEXT_FONT,
            text_filling_ratio=0.8,
            font_size_title=MAIN_BUTTON_FONT_SIZE,
            font_size_content=CONTENT_LABEL_FONT_SIZE,
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
        self.title = title
        self.content = content
        self.text_filling_ratio = text_filling_ratio
        self.font_size_title = font_size_title
        self.font_size_content = font_size_content

    def on_press(self):
        if self.button_mode:
            self.opacity = OPACITY_ON_BUTTON_PRESS

    def on_release(self):
        if self.button_mode:
            self.release_function()
            self.opacity = 1
