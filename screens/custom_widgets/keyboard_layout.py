"""
Module to create the theme selection layout.
"""

###############
### Imports ###
###############

### Python imports ###

from functools import partial

### Kivy imports ###

from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import (
    StringProperty,
    NumericProperty,
    ColorProperty,
    ObjectProperty
)

### Local imports ###

from tools.path import (
    PATH_TEXT_FONT
)
from tools.constants import (
    CUSTOMIZATION_LAYOUT_FONT_SIZE,
    THEMES_DICT,
    LETTER_FONT_SIZE
)
from screens.custom_widgets import (
    ColoredRoundedButton
)

#############
### Class ###
#############


class KeyboardLayout(RelativeLayout):
    """
    The keyboard layout.
    """

    font_size = NumericProperty()
    font_ratio = NumericProperty(1)
    horizontal_padding = NumericProperty(0.2/9)
    size_letter = NumericProperty(0.08)
    text_font_name = StringProperty()
    background_color = ColorProperty([1, 1, 1, 1])
    touch_color = ColorProperty([0, 0, 0, 1])
    type_keyboard = StringProperty("QWERTY")
    touch_function = ObjectProperty()

    def __init__(
            self,
            text_font_name=PATH_TEXT_FONT,
            font_size=CUSTOMIZATION_LAYOUT_FONT_SIZE,
            font_ratio=None,
            **kwargs):

        if font_ratio is not None:
            self.font_ratio = font_ratio

        self.bind(background_color=self.bind_function)
        self.bind(touch_color=self.bind_function)
        self.bind(type_keyboard=self.bind_function)
        self.bind(horizontal_padding=self.bind_function)
        self.bind(touch_function=self.bind_function)

        super().__init__(**kwargs)
        self.text_font_name = text_font_name
        self.font_size = font_size

    def bind_function(self, base_widget, value):
        pass

    def update_padding(self, base_widget, value):
        self.size_letter = (1 - self.horizontal_padding*9)/10 # because maximum of 9 letters in line

    def build_keyboard(self):
        vertical_padding = 0.05
        height_letter = (1-vertical_padding*3) / 3

        if self.type_keyboard == "QWERTY":
            first_line_letters = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"]
            second_line_letters = ["A", "S", "D", "F", "G", "H", "J", "K", "L"]
            third_line_letters = ["Z", "X", "C", "V", "B", "N", "M"]
            first_margin = 0
            second_margin = (self.size_letter+self.horizontal_padding)/2
            third_margin = (self.size_letter+self.horizontal_padding)/2
        elif self.type_keyboard == "AZERTY":
            first_line_letters = ["A", "Z", "E", "R", "T", "Y", "U", "I", "O", "P"]
            second_line_letters = ["Q", "S", "D", "F", "G", "H", "J", "K", "L", "M"]
            third_line_letters = ["W", "X", "C", "V", "B", "N"]
            first_margin = 0
            second_margin = 0
            third_margin = self.size_letter+self.horizontal_padding

        # First line
        counter = 0
        for letter in first_line_letters:
            colored_rounded_button = ColoredRoundedButton(
                text=letter,
                background_color=self.background_color,
                touch_color=self.touch_color,
                pos_hint={
                    "x": first_margin+counter*self.horizontal_padding+counter*self.size_letter,
                    "y": 2*vertical_padding + 2*height_letter},
                font_size=LETTER_FONT_SIZE,
                font_ratio=self.font_ratio,
                size_hint=(self.size_letter, height_letter),
                color_label=(1,1,1,1),
                on_release=partial(self.touch_letter, letter)
            )
            self.add_widget(colored_rounded_button)
            counter += 1

        # Second line
        counter = 0
        for letter in second_line_letters:
            colored_rounded_button = ColoredRoundedButton(
                text=letter,
                background_color=self.background_color,
                touch_color=self.touch_color,
                pos_hint={
                    "x": second_margin+counter*self.horizontal_padding+counter*self.size_letter,
                    "y": vertical_padding + height_letter},
                font_size=LETTER_FONT_SIZE,
                font_ratio=self.font_ratio,
                size_hint=(self.size_letter, height_letter),
                color_label=(1,1,1,1),
                on_release=partial(self.touch_letter, letter)
            )
            self.add_widget(colored_rounded_button)
            counter += 1

        # Third line
        counter = 0
        for letter in third_line_letters:
            colored_rounded_button = ColoredRoundedButton(
                text=letter,
                background_color=self.background_color,
                touch_color=self.touch_color,
                pos_hint={
                    "x": third_margin+counter*self.horizontal_padding+counter*self.size_letter,
                    "y": 0},
                font_size=LETTER_FONT_SIZE,
                font_ratio=self.font_ratio,
                size_hint=(self.size_letter, height_letter),
                color_label=(1,1,1,1),
                on_release=partial(self.touch_letter, letter)
            )
            self.add_widget(colored_rounded_button)
            counter += 1

        # BACK key
        back_key = ColoredRoundedButton(
            text="BACK",
            background_color=self.background_color,
            touch_color=self.touch_color,
            pos_hint={
                "x": third_margin+counter*self.horizontal_padding+counter*self.size_letter,
                "y": 0},
            font_size=LETTER_FONT_SIZE,
            font_ratio=self.font_ratio,
            size_hint=(self.size_letter*2+self.horizontal_padding, height_letter),
            color_label=(1,1,1,1),
            on_release=partial(self.touch_letter, "BACK")
        )
        self.add_widget(back_key)

    def touch_letter(self, letter, *args):
        self.touch_function(letter)
