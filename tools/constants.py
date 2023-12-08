"""
Module referencing the main constants of the application.

Constants
---------
__version__ : str
    Version of the application.

MOBILE_MODE : bool
    Whether the application is launched on mobile or not.
"""

###############
### Imports ###
###############

### Python imports ###

import os

### Kivy imports ###

from kivy import platform

### Module imports ###

from tools.path import (
    PATH_USER_DATA,
    PATH_WORDS
)
from tools.basic_tools import (
    load_json_file,
    save_json_file
)

#################
### Constants ###
#################

### Version ###

__version__ = "1.0.0"

### Mode ###

MOBILE_MODE = platform == "android"
DEBUG_MODE = False
FPS = 30
MSAA_LEVEL = 2
BACK_ARROW_SIZE = 0.2

### Data loading ###

# Create the user data json if it does not exist
if not os.path.exists(PATH_USER_DATA):
    default_user_data = {
        "free_mode": {},
        "daily_mode": {
            "start_word": "",
            "end_word": ""
        },
        "history": {},
        "items": {
            "coins": 0,
            "unlocked_backgrounds": [],
            "unlocked_palettes": [],
            "unlocked_musics": []
        },
        "settings": {
            "sound_volume": 0.5,
            "music_volume": 0.5,
            "current_background": "",
            "current_music": "",
            "current_palette": ""
        }
    }
    save_json_file(PATH_USER_DATA, default_user_data)

# Load the data of the user


class UserData():
    """
    A class to store the user data.
    """

    def __init__(self) -> None:
        data = load_json_file(PATH_USER_DATA)
        self.free_mode = data["free_mode"]
        self.daily_mode = data["daily_mode"]
        self.history = data["history"]
        self.settings = data["settings"]
        self.items = data["items"]

    def save_changes(self) -> None:
        """
        Save the changes in the data.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """

        # Create the dictionary of data
        data = {}
        data["free_mode"] = self.free_mode
        data["daily_mode"] = self.daily_mode
        data["history"] = self.history
        data["settings"] = self.settings
        data["items"] = self.items

        # Save this dictionary
        save_json_file(
            file_path=PATH_USER_DATA,
            dict_to_save=data)


USER_DATA = UserData()

### Colors ###


class ColorPalette():
    """
    Class to store the colors used in the screens.
    """

    def __init__(self) -> None:
        self.PRIMARY = (0, 0, 0, 1)
        self.SECONDARY = (0, 0, 0, 1)


TEXT_FONT_COLOR = (0, 0, 0, 1)

### Musics ###

SOUND_LIST = []


### Ads code ###

REWARD_INTERSTITIAL = ""
INTERSTITIAL = ""

### Words loading ###


with open(PATH_WORDS) as file:
    ENGLISH_WORDS = []
    for i, line in enumerate(file):
        ENGLISH_WORDS.append(line.replace("\n", ""))
