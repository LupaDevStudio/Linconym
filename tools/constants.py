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

### Local imports ###

from tools.path import (
    PATH_USER_DATA,
    PATH_WORDS_10K,
    PATH_WORDS_34K,
    PATH_WORDS_88K,
    PATH_WORDS_375K,
    PATH_GAMEPLAY,
    PATH_THEMES
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
        self.unlocked_themes = data["unlocked_themes"]
        self.unlocked_musics = data["unlocked_musics"]
        self.user_profile = data["user_profile"]

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
        data["unlocked_themes"] = self.unlocked_themes
        data["unlocked_musics"] = self.unlocked_musics
        data["user_profile"] = self.user_profile

        # Save this dictionary
        save_json_file(
            file_path=PATH_USER_DATA,
            dict_to_save=data)

    def change_theme_image(self, theme):
        USER_DATA.settings["current_theme_image"] = theme
        self.save_changes()

    def change_theme_colors(self, theme):
        USER_DATA.settings["current_theme_colors"] = theme
        self.save_changes()

    def buy_item(self, theme, item_type, price):
        if self.user_profile["coins"] >= price:
            self.user_profile["coins"] = self.user_profile["coins"] - price
            if item_type == "music":
                self.unlocked_musics[theme] = True
            elif item_type == "image":
                if theme not in self.unlocked_themes:
                    self.unlocked_themes[theme] = {
                        "image": False,
                        "colors": False}
                self.unlocked_themes[theme]["image"] = True
            elif item_type == "colors":
                if theme not in self.unlocked_themes:
                    self.unlocked_themes[theme] = {
                        "image": False,
                        "colors": False}
                self.unlocked_themes[theme]["colors"] = True
            else:
                raise ValueError("Unrecognized item type.")
            self.save_changes()
            return True
        return False


USER_DATA = UserData()

### Colors ###


class ColorPalette():
    """
    Class to store the colors used in the screens.
    """

    def __init__(self) -> None:
        self.PRIMARY = (0, 0, 0, 1)
        self.SECONDARY = (0, 0, 0, 1)

### Graphics ###


TEXT_FONT_COLOR = (0, 0, 0, 1)
TITLE_FONT_SIZE = 45
TITLE_OUTLINE_WIDTH = 2
TITLE_OUTLINE_COLOR = (1, 1, 1, 1)
MAIN_BUTTON_FONT_SIZE = 30
CONTENT_LABEL_FONT_SIZE = 17
ACT_BUTTON_FONT_SIZE = 25
BOTTOM_BAR_HEIGHT = 0.12
CUSTOM_BUTTON_BACKGROUND_COLOR = (1, 1, 1, 0.7)
MAIN_COLOR = (1, 0, 0, 1)
SECOND_COLOR = (0, 0, 0, 1)
OPACITY_ON_BUTTON_PRESS = 0.8
CUSTOMIZATION_LAYOUT_FONT_SIZE = 20
COINS_COUNT_FONT_SIZE = 22
POS_HINT_BACK_ARROW = {"x":0.02, "top":0.99}

### Musics ###

SOUND_LIST = []

### Ads code ###

REWARD_INTERSTITIAL = ""
INTERSTITIAL = ""

### Words loading ###

with open(PATH_WORDS_10K) as file:
    ENGLISH_WORDS_10K = []
    for i, line in enumerate(file):
        ENGLISH_WORDS_10K.append(line.replace("\n", ""))

with open(PATH_WORDS_34K) as file:
    ENGLISH_WORDS_34K = []
    for i, line in enumerate(file):
        ENGLISH_WORDS_34K.append(line.replace("\n", ""))

with open(PATH_WORDS_88K) as file:
    ENGLISH_WORDS_88K = []
    for i, line in enumerate(file):
        ENGLISH_WORDS_88K.append(line.replace("\n", ""))

with open(PATH_WORDS_375K) as file:
    ENGLISH_WORDS_375K = []
    for i, line in enumerate(file):
        ENGLISH_WORDS_375K.append(line.replace("\n", ""))

ENGLISH_WORDS_DICTS = {
    "10k": ENGLISH_WORDS_10K,
    "34k": ENGLISH_WORDS_34K,
    "88k": ENGLISH_WORDS_88K,
    "375k": ENGLISH_WORDS_375K
}

### Levels ###

GAMEPLAY_DICT = load_json_file(PATH_GAMEPLAY)

### Themes ###

THEMES_DICT = load_json_file(PATH_THEMES)
