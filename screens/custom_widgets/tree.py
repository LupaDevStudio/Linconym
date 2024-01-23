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
from kivy.properties import (
    NumericProperty,
    ListProperty
)

### Local imports ###

from tools.basic_tools import argsort

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

#############
### Class ###
#############


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

    # def change_current_position()

    def build_layout(
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

        # Extract and sort the positions to make sure parents are treated before there children
        positions_list = list(position_to_word_id.keys())

        def key(x: str):
            return (len(x.split(",")), convert_str_position_to_tuple_position(x))
        sorted_positions_indices = argsort(positions_list, key=key)
        sorted_positions_list = [positions_list[i]
                                 for i in sorted_positions_indices]

        # Define variables for the loop
        previous_rank = 0

        # Iterate over the positions to display the widgets
        for position in sorted_positions_list:

            # Set the current rank
            current_rank = len(position.split(","))

            # Reset the vertical offset if a new colum is starting
            if current_rank > previous_rank:
                current_vertical_offset = 0
                previous_rank = current_rank

            # Extract the corresponding word
            word_id = position_to_word_id[position]
            word = words_found[word_id]

            # Find the number of children
            nb_children = 0
            for temp_position in sorted_positions_list:
                if temp_position in position and len(temp_position) > len(position):
                    nb_children += 1

            # Add the word widget
            ...

            # Add the link with the parent
            ...

            # Update the vertical offset
            current_vertical_offset += 1 + nb_children
