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

    main_color = ObjectProperty()
    background_color = ObjectProperty()

    def __init__(
            self,
            value=0.5,
            main_color=MAIN_COLOR,
            background_color=SECOND_COLOR,
            **kwargs):
        super().__init__(**kwargs)

        self.main_color = main_color
        self.background_color = background_color
        self.value = value
