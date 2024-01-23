"""
Module to create the tree to display the user progress on a level.
"""

###############
### Imports ###
###############

### Kivy imports ###
from kivy.uix.scrollview import ScrollView
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import (
    NumericProperty,
    ListProperty
)

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
