"""
Module to create the tree to display the user progress on a level.
"""

###############
### Imports ###
###############

### Python imports ###

from typing import (
    Dict,
    List
)

### Kivy imports ###

from kivy.uix.scrollview import ScrollView
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import (
    StringProperty,
    NumericProperty,
    BooleanProperty,
    ColorProperty,
    ListProperty
)

### Local imports ###

from tools.basic_tools import argsort
from tools.path import (
    PATH_TEXT_FONT
)
from tools.constants import (
    MAIN_BUTTON_FONT_SIZE,
)

#################
### Functions ###
#################


def convert_str_position_to_tuple_position(str_position: str):
    """
    Convert a position under a string format to a tuple format.

    Parameters
    ----------
    str_position : str
        Position in a string format.

    Returns
    -------
    tuple
        Position in a tuple format.
    """

    str_elts = str_position.split(",")
    res = []
    for elt in str_elts:
        res.append(int(elt))
    res = tuple(res)

    return res


def build_sorted_positions_list(position_to_word_id: Dict[str, int]):
    """
    Extract and sort the positions to make sure parents are treated before there children.
    """

    positions_list = list(position_to_word_id.keys())

    print(positions_list)

    def key(x: str):
        print(x)
        return (len(x[1].split(",")), convert_str_position_to_tuple_position(x[1]))
    # sorted_positions_indices = argsort(positions_list, key=key)
    sorted_positions_indices = argsort(positions_list)
    sorted_positions_list = [positions_list[i]
                             for i in sorted_positions_indices]

    return sorted_positions_list

###############
### Classes ###
###############


class WordButton(ButtonBehavior, RelativeLayout):
    """
    A custom button with a colored round rectangle background.
    """

    background_color = ColorProperty()
    touch_color = ColorProperty()
    outline_color = ColorProperty()
    text = StringProperty()
    text_filling_ratio = NumericProperty()
    font_size = NumericProperty()
    font_ratio = NumericProperty(1)
    disable_button = BooleanProperty(False)
    text_font_name = StringProperty(PATH_TEXT_FONT)

    def __init__(
            self,
            text_font_name=PATH_TEXT_FONT,
            text_filling_ratio=0.8,
            release_function=lambda: 1 + 1,
            font_ratio=None,
            **kwargs):
        if font_ratio is not None:
            self.font_ratio = font_ratio
        super().__init__(**kwargs)
        self.release_function = release_function
        self.always_release = True
        self.text_font_name = text_font_name
        self.text_filling_ratio = text_filling_ratio

    def on_press(self):
        if not self.disable_button:
            self.temp_color = self.background_color
            self.background_color = self.touch_color

    def on_release(self):
        if not self.disable_button:
            self.background_color = self.temp_color
            self.release_function()


class TreeScrollview(ScrollView):
    """
    Class containing the scrollview to scroll over the tree.
    """


class TreeLayout(RelativeLayout):
    """
    Class to create a tree layout to contain the user progress.
    """

    primary_color = ListProperty([0.5, 0.5, 0.5, 1.])
    secondary_color = ListProperty([1., 1., 1., 1.])

    def __init__(
            self,
            **kwargs):
        super().__init__(**kwargs)
        self.size_hint_y = (None)
        self.size_hint_x = (None)
        self.bind(primary_color=self.on_primary_color_change)
        self.on_primary_color_change()

    def on_primary_color_change(self, base=None, widget=None, value=None):
        self.transparent_primary_color = (
            self.primary_color[0], self.primary_color[1], self.primary_color[2], 0.7)

    def change_current_position():
        pass

    def build_layout(
            self,
            position_to_word_id: Dict[str, int],
            words_found: List[str],
            current_position: str):
        """
        Build the layout of the tree.

        Parameters
        ----------
        position_to_word_id : Dict[str, int]
            _description_
        words_found : List[str]
            _description_
        current_position : str
            _description_
        """

        sorted_positions_list = build_sorted_positions_list(
            position_to_word_id)

        # Define the initial vertical offset
        current_vertical_offset = 0

        # Define the intial value for the previous rank
        previous_rank = -1

        # Create a dict to store the grid positions to plot the links
        position_to_grid_position = {}

        # Iterate over the positions to display the widgets
        for position in sorted_positions_list:

            # Set the current rank
            current_rank = len(position.split(","))

            if current_rank <= previous_rank:
                current_vertical_offset += 1

            # Extract the corresponding word
            word_id = position_to_word_id[position]
            word = words_found[word_id]

            # Add the word widget
            word_widget = WordButton(
                text=word,
                background_color=self.primary_color,
                touch_color=self.transparent_primary_color
            )

            # Add the link with the parent
            ...

            # Store the grid position
            position_to_grid_position[position] = (
                current_rank, current_vertical_offset)

            # Update the previous rank
            previous_rank = current_rank

###############
### Testing ###
###############


test_words_found = ["sea", "sale", "sell", "shell", "sail", "snail",
                    "see", "bee", "tea", "pea", "peak", "keep", "tape", "pelt", "apes"]

test_position_to_word_id = {"0": 0, "0,0": 1, "0,0,0": 2,
                            "0,0,0,0": 3, "0,0,1": 4, "0,0,1,0": 5, "0,1": 6, "0,1,0": 7, "0,2": 8, "0,3": 9, "0,3,0": 10, "0,3,0,0": 11, "0,3,1": 12, "0,3,1,0": 13, "0,3,2": 14}

if __name__ == "__main__":
    print(build_sorted_positions_list(test_position_to_word_id))
