"""
Module to create three stars with a certain filling ratio
"""

###############
### Imports ###
###############

### Kivy imports ###
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import (
    NumericProperty,
    ListProperty
)

#############
### Class ###
#############


class ThreeStars(RelativeLayout):
    """
    Class to create a widget with three stars that can be turn on and off.
    """

    star_one_color = ListProperty([0.5, 0.5, 0.5, 1.])
    star_two_color = ListProperty([0.5, 0.5, 0.5, 1.])
    star_three_color = ListProperty([0.5, 0.5, 0.5, 1.])
    star_color_dict = {1: star_one_color,
                       2: star_two_color,
                       3: star_three_color}
    stars_number = NumericProperty()
    primary_color = ListProperty([0.5, 0.5, 0.5, 1.])
    secondary_color = ListProperty([1., 1., 1., 1.])

    def __init__(
            self,
            primary_color=[1., 1., 1., 1.],
            secondary_color=[0.5, 0.5, 0.5, 1.],
            **kwargs):

        self.primary_color = primary_color
        self.secondary_color = secondary_color

        self.bind(stars_number=self.change_stars_number)
        super().__init__(**kwargs)

    def change_stars_number(self, base_widget, value):
        """
        Change the number of stars displayed.
        """

        # self.stars_number = stars_number
        if self.stars_number > 0:
            self.star_one_color = self.primary_color
        else:
            self.star_one_color = self.secondary_color
        if self.stars_number > 1:
            self.star_two_color = self.primary_color
        else:
            self.star_two_color = self.secondary_color
        if self.stars_number > 2:
            self.star_three_color = self.primary_color
        else:
            self.star_three_color = self.secondary_color
