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
    ColorProperty
)

#############
### Class ###
#############


class CustomProgressBar(Widget):
    """
    A custom button with a white round rectangle background.
    """

    primary_color = ColorProperty()
    secondary_color = ColorProperty()

    def __init__(
            self,
            value=0.5,
            **kwargs):
        super().__init__(**kwargs)

        self.bind(primary_color = self.my_function)
        self.bind(secondary_color = self.my_function)
        self.value = value

    def my_function(self, base_widget, value):
        pass
