"""
Module to create the bottom bar with the buttons.
"""

###############
### Imports ###
###############

from kivy.uix.relativelayout import RelativeLayout
from tools.kivy_tools import ImageButton

#############
### Class ###
#############


class BottomBar(RelativeLayout):
    background_color = (0, 0, 0, 0.5)
    separation_color = (1, 1, 1, 1)
    separation_height = 3
    button_width = 0.15
    button_height = 0.7
