"""
Module to create the act button.
"""

###############
### Imports ###
###############

### Kivy imports ###
from kivy.uix.image import Image
from kivy.properties import (
    StringProperty,
    NumericProperty,
    ObjectProperty,
    BooleanProperty
)

### Local imports ###

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


class ThemeLayout(Image):
    """
    A layout to display the customization to buy.
    """

    theme_title = StringProperty()
    font_size = NumericProperty()
    font_ratio = NumericProperty()
    text_font_name = StringProperty()
    main_color = ObjectProperty()
    second_color = ObjectProperty()
    has_bought_image = BooleanProperty()
    has_bought_colors = BooleanProperty()
    is_using_image = BooleanProperty()
    is_using_colors = BooleanProperty()

    def __init__(
            self,
            theme_title: str = "",
            text_font_name=PATH_TEXT_FONT,
            font_size=CUSTOMIZATION_LAYOUT_FONT_SIZE,
            main_color=MAIN_COLOR,
            second_color=SECOND_COLOR,
            has_bought_image:bool = False,
            has_bought_colors:bool = False,
            is_using_image:bool = False,
            is_using_colors:bool = False,
            font_ratio=None,
            **kwargs):

        self.theme_title = theme_title
        if font_ratio is not None:
            self.font_ratio = font_ratio

        super().__init__(**kwargs)
        self.text_font_name = text_font_name
        self.font_size = font_size
        self.main_color = main_color
        self.second_color = second_color
        self.has_bought_image = has_bought_image
        self.has_bought_colors = has_bought_colors
        self.is_using_image = is_using_image
        self.is_using_colors = is_using_colors
