"""
Module to manage colors with kivy.
"""

#################
### Functions ###
#################


def change_color_opacity(color, opacity):
    new_color = (color[0], color[1], color[2], opacity)
    return new_color
