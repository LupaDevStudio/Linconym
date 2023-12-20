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
    BooleanProperty,
    ListProperty,
    ColorProperty
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
    primary_color = ColorProperty([1, 1, 1, 1])
    secondary_color = ColorProperty([0, 0, 0, 1])
    has_bought_image = BooleanProperty()
    has_bought_colors = BooleanProperty()
    is_using_image = BooleanProperty()
    is_using_colors = BooleanProperty()

    def __init__(
            self,
            theme_title: str = "",
            text_font_name=PATH_TEXT_FONT,
            font_size=CUSTOMIZATION_LAYOUT_FONT_SIZE,
            primary_color=MAIN_COLOR,
            secondary_color=SECOND_COLOR,
            has_bought_image: bool = False,
            has_bought_colors: bool = False,
            is_using_image: bool = False,
            is_using_colors: bool = False,
            image_price: int = 0,
            colors_price: int = 0,
            font_ratio=None,
            **kwargs):

        self.theme_title = theme_title
        if font_ratio is not None:
            self.font_ratio = font_ratio

        self.primary_color = primary_color
        self.secondary_color = secondary_color

        super().__init__(**kwargs)
        self.text_font_name = text_font_name
        self.font_size = font_size

        self.has_bought_image = has_bought_image
        self.has_bought_colors = has_bought_colors
        self.is_using_image = is_using_image
        self.is_using_colors = is_using_colors

        self.image_price = image_price
        self.colors_price = colors_price

    def update_display(self):
        self.ids["buy_image_button"].price = self.image_price
        self.ids["buy_image_button"].update_display()
        self.ids["buy_colors_button"].price = self.colors_price
        self.ids["buy_colors_button"].update_display()

    def click_image(self):
        print("image")
        pass

    def click_colors(self):
        print("colors")
        pass
