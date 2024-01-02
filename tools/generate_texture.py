"""
Module to generate texture during the execution.
"""

###############
### Imports ###
###############

### Python imports ###
from PIL import Image as PIL_Image
from PIL import ImageDraw

### Local imports ###
from tools.path import PATH_TEMP_IMAGES

#################
### Constants ###
#################

INNER_SPINNER_CIRCLE_RADIUS = 100
SPINNER_CIRCLE_OUTSIDE_WIDTH = 10
SPINNER_RECTANGLE_OUTSIDE_WIDTH = 10
SPINNER_RECTANGLE_HEIGHT = 60

#################
### Functions ###
#################


def convert_1_to_255(arg):
    return int(arg * 255)


def generate_spinner_cirle(primary_color, secondary_color, save_int=0):
    """
    Generate the spinner circle texture with the given colors.

    Parameters
    ----------
    primary_color : tuple
        Primary color to use.
    secondary_color : tuple
        Secondary color to use.

    Returns
    -------
    None
    """
    spinner_texture = PIL_Image.new("RGBA", (256, 256), (0, 0, 0, 0))
    draw = ImageDraw.Draw(spinner_texture)
    draw.ellipse((0, 0, 256, 256), fill=primary_color,
                 outline=secondary_color, width=SPINNER_CIRCLE_OUTSIDE_WIDTH)
    draw.ellipse((128 - INNER_SPINNER_CIRCLE_RADIUS // 2, 128 - INNER_SPINNER_CIRCLE_RADIUS //
                 2, 128 + INNER_SPINNER_CIRCLE_RADIUS // 2, 128 + INNER_SPINNER_CIRCLE_RADIUS // 2), fill=secondary_color)
    spinner_texture.save(PATH_TEMP_IMAGES + f"circle_{save_int}.png")


def generate_spinner_rectangle(primary_color, secondary_color, save_int=0):
    """
    Generate the spinner rectangle texture with the given colors.

    Parameters
    ----------
    primary_color : tuple
        Primary color to use.
    secondary_color : tuple
        Secondary color to use.

    Returns
    -------
    None
    """
    spinner_texture = PIL_Image.new("RGBA", (256, 256), (0, 0, 0, 0))
    draw = ImageDraw.Draw(spinner_texture)
    draw.rectangle((0,
                   128 - SPINNER_RECTANGLE_HEIGHT // 2, 256, 128 + SPINNER_RECTANGLE_HEIGHT // 2), fill=secondary_color)
    draw.rectangle((0,
                    128 - SPINNER_RECTANGLE_HEIGHT // 2 - SPINNER_RECTANGLE_OUTSIDE_WIDTH // 2,
                    256,
                    128 - SPINNER_RECTANGLE_HEIGHT // 2 + SPINNER_RECTANGLE_OUTSIDE_WIDTH // 2),
                   fill=primary_color)
    draw.rectangle((0,
                    128 + SPINNER_RECTANGLE_HEIGHT // 2 - SPINNER_RECTANGLE_OUTSIDE_WIDTH // 2,
                    256,
                    128 + SPINNER_RECTANGLE_HEIGHT // 2 + SPINNER_RECTANGLE_OUTSIDE_WIDTH // 2),
                   fill=primary_color)
    spinner_texture.save(PATH_TEMP_IMAGES + f"rectangle_{save_int}.png")


def generate_spinner_texture(primary_color, secondary_color, save_int=0):
    """
    Generate the textures for the spinner.

    Parameters
    ----------
    primary_color : tuple
        Primary color.
    secondary_color : tuple
        Secondary color.

    Returns
    -------
    """
    generate_spinner_cirle(primary_color=primary_color,
                           secondary_color=secondary_color, save_int=save_int)
    generate_spinner_rectangle(
        primary_color=primary_color, secondary_color=secondary_color, save_int=save_int)


if __name__ == "__main__":
    generate_spinner_cirle(primary_color=(155, 100, 20),
                           secondary_color=(200, 200, 200))
    generate_spinner_rectangle(primary_color=(155, 100, 20),
                               secondary_color=(200, 200, 200))
