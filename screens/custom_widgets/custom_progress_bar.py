"""
Module to create custom progress bar.
"""

###############
### Imports ###
###############

### Kivy imports ###

from kivy.uix.widget import (
    Widget
)
from kivy.properties import (
    ObjectProperty
)

### Local imports ###

from tools.constants import (
    MAIN_COLOR,
    SECOND_COLOR
)

#############
### Class ###
#############


class CustomProgressBar(Widget):
    """
    A custom button with a white round rectangle background.
    """

    primary_color = ObjectProperty()
    background_color = ObjectProperty()

    def __init__(
            self,
            value=0.5,
            primary_color=MAIN_COLOR,
            background_color=SECOND_COLOR,
            **kwargs):
        super().__init__(**kwargs)

        self.primary_color = primary_color
        self.background_color = background_color
        self.value = value
