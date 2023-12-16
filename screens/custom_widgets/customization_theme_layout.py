"""
Module to create the act button.
"""

###############
### Imports ###
###############

### Python imports ###
from typing import Literal

### Kivy imports ###
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import (
    StringProperty,
    NumericProperty,
    ObjectProperty,
    BooleanProperty
)

### Module imports ###

from tools.path import (
    PATH_TEXT_FONT
)
from tools.constants import (
    MAIN_COLOR,
    SECOND_COLOR,
    CUSTOMIZATION_LAYOUT_FONT_SIZE
)

#############
### Class ###
#############


class CustomizationThemeLayout(RelativeLayout):
    """
    A layout to display the customization to buy.
    """

    background_image = StringProperty()
    theme_title = StringProperty()
    font_size = NumericProperty()
    font_ratio = NumericProperty()
    text_font_name = StringProperty()
    main_color = ObjectProperty()
    second_color = ObjectProperty()
    has_bought_image = BooleanProperty()
    has_bought_colors = BooleanProperty()

    def __init__(
            self,
            theme_title: str = "",
            parent=None,
            text_font_name=PATH_TEXT_FONT,
            font_size=CUSTOMIZATION_LAYOUT_FONT_SIZE,
            background_image: str = "",
            main_color=MAIN_COLOR,
            second_color=SECOND_COLOR,
            has_bought_image:bool = False,
            has_bought_colors:bool = False,
            font_ratio=None,
            **kwargs):

        self.theme_title = theme_title
        if parent is not None:
            self.parent = parent
        if font_ratio is not None:
            self.font_ratio = font_ratio

        super().__init__(**kwargs)
        self.text_font_name = text_font_name
        self.font_size = font_size
        self.background_image = background_image
        self.main_color = main_color
        self.second_color = second_color
        self.has_bought_image = has_bought_image
        self.has_bought_colors = has_bought_colors

