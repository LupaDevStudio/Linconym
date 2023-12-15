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
    nb_stars = NumericProperty()
    primary_color = ListProperty([0.5, 0.5, 0.5, 1.])
    secondary_color = ListProperty([1., 1., 1., 1.])

    def __init__(
            self,
            primary_color=[1., 1., 1., 1.],
            secondary_color=[0.5, 0.5, 0.5, 1.],
            **kwargs):

        self.primary_color = primary_color
        self.secondary_color = secondary_color

        self.bind(nb_stars=self.change_nb_stars)
        super().__init__(**kwargs)

    def change_nb_stars(self, base_widget, value):
        """
        Change the number of stars displayed.
        """

        # self.nb_stars = nb_stars
        if self.nb_stars > 0:
            self.star_one_color = self.primary_color
        else:
            self.star_one_color = self.secondary_color
        if self.nb_stars > 1:
            self.star_two_color = self.primary_color
        else:
            self.star_two_color = self.secondary_color
        if self.nb_stars > 2:
            self.star_three_color = self.primary_color
        else:
            self.star_three_color = self.secondary_color
