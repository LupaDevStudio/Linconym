"""
Module to create the act button.
"""

###############
### Imports ###
###############

from functools import partial

### Kivy imports ###
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import (
    StringProperty,
    NumericProperty,
    ListProperty,
    ColorProperty,
    BooleanProperty
)

### Local imports ###

from tools.path import (
    PATH_TITLE_FONT
)
from tools.constants import (
    CUSTOMIZATION_LAYOUT_FONT_SIZE,
    CUSTOM_BUTTON_BACKGROUND_COLOR
)

#############
### Class ###
#############


class BoosterLayout(RelativeLayout):
    """
    A layout to display the boosters.
    """

    background_color = CUSTOM_BUTTON_BACKGROUND_COLOR
    mode = StringProperty() # can be "ads" or "buy"
    booster_title = StringProperty()
    font_size = NumericProperty()
    font_ratio = NumericProperty(1)
    text_font_name = StringProperty()
    list_ads_buy = ListProperty()
    first_color = ColorProperty((1, 1, 1, 1))
    second_color = ColorProperty((0, 0, 0, 1))
    third_color = ColorProperty((0, 0, 0, 1))
    first_disable = BooleanProperty()
    second_disable = BooleanProperty()
    third_disable = BooleanProperty()

    def __init__(
            self,
            text_font_name=PATH_TITLE_FONT,
            font_size=CUSTOMIZATION_LAYOUT_FONT_SIZE,
            font_ratio=None,
            **kwargs):
        super().__init__(**kwargs)

        if font_ratio is not None:
            self.font_ratio = font_ratio

        self.text_font_name = text_font_name
        self.font_size = font_size
        self.bind(mode=self.bind_function)
        self.bind(booster_title=self.bind_function)
        self.bind(list_ads_buy=self.update_colors_disabled)

    def bind_function(self, base_widget, value):
        pass

    def update_colors_disabled(self, base_widget, value):
        for counter in range(len(self.list_ads_buy)):
            element = self.list_ads_buy[counter]
            if counter == 0:
                self.first_color = element["color"]
                self.first_disable = element["disable_button"]
            elif counter == 1:
                self.second_color = element["color"]
                self.second_disable = element["disable_button"]
            elif counter == 2:
                self.third_color = element["color"]
                self.third_disable = element["disable_button"]
        self.ids.first_circle.release_function = partial(self.choose_item, 1)
        self.ids.second_circle.release_function = partial(self.choose_item, 2)
        self.ids.third_circle.release_function = partial(self.choose_item, 3)

    def choose_item(self, number):
        if self.mode == "ads":
            self.parent.see_ad(number)
        elif self.mode == "buy":
            self.parent.buy_booster(number)
