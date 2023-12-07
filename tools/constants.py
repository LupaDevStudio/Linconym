"""
Module referencing the main constants of the application.

Constants
---------
__version__ : str
    Version of the application.

MOBILE_MODE : bool
    Whether the application is launched on mobile or not.

PATH_RESOURCES_FOLDER : str
    Path to the resources folder.

PATH_LANGUAGE : str
    Path to the folder where are stored the json files of language.

PATH_APP_IMAGES : str
    Path to the folder where are stored the images for the application.

PATH_KIVY_FOLDER : str
    Path to the folder where are stored the different kv files.

DICT_LANGUAGE_CORRESPONDANCE : dict
    Dictionary associating the language to its code.
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
    PATH_LANGUAGE
)
from tools.basic_tools import (
    load_json_file,
    save_json_file
)

#################
### Constants ###
#################

### Version ###

__version__ = "2.0.2"

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
        "language": "english",
        "highscore": 0,
        "endings": {
            "order_max": False,
            "order_min": False,
            "military_max": False,
            "military_min": False,
            "civilian_max": False,
            "civilian_min": False,
            "paleo_max": False,
            "paleo_min": False,
            "food": False,
            "weapons": False,
            "tools": False,
        },
        "tutorial": True,
        "music_volume": 0.5,
        "sound_effects_volume": 0.5
    }
    save_json_file(PATH_USER_DATA, default_user_data)

# Load the data of the user


class UserData():
    """
    A class to store the user data.
    """

    def __init__(self) -> None:
        data = load_json_file(PATH_USER_DATA)
        self.language = data["language"]
        self.highscore = data["highscore"]
        self.endings = data["endings"]
        self.tutorial = data["tutorial"]
        self.music_volume = data["music_volume"]
        self.sound_effects_volume = data["sound_effects_volume"]

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
        data["language"] = self.language
        data["highscore"] = self.highscore
        data["endings"] = self.endings
        data["tutorial"] = self.tutorial
        data["music_volume"] = self.music_volume
        data["sound_effects_volume"] = self.sound_effects_volume

        # Save this dictionary
        save_json_file(
            file_path=PATH_USER_DATA,
            dict_to_save=data)


USER_DATA = UserData()

### Language ###

DICT_LANGUAGE_CORRESPONDANCE = {
    "french": "Français",
    "english": "English"
}
DICT_LANGUAGE_NAME_TO_CODE = {
    "Français": "french",
    "English": "english"
}
LANGUAGES_LIST = tuple(DICT_LANGUAGE_CORRESPONDANCE.values())


class Text():
    def __init__(self, language) -> None:
        self.language = language
        self.change_language(language)

    def change_language(self, language):
        """
        Change the language of the text contained in the class.
        """
        # Change the language
        self.language = language

        # Load the json file
        data = load_json_file(PATH_LANGUAGE + language + ".json")

        # Split the text contained in the screens
        self.menu = data["menu"]
        self.settings = data["settings"]
        self.game_over = data["game_over"]
        self.game = data["game"]
        self.tutorial = data["introduction"] + data["tutorial"]

        # Split the text for the cards
        self.decision = data["decision"]
        self.event = data["event"]
        self.ending = data["ending"]
        self.decree = data["decree"]
        self.answer = data["answer"]


TEXT = Text(language=USER_DATA.language)

### Colors ###

BACKGROUND_COLOR = (0, 0, 0, 1)
TITLE_FONT_COLOR = (0, 0, 0, 1)
TEXT_FONT_COLOR = (0, 0, 0, 1)

### Musics ###

MUSIC_LIST = ["game_music.mp3", "time_of_the_apocalypse.mp3"]
SOUND_LIST = ["decision.wav", "decree.wav", "guillotine.wav"]
START_MUSIC_LIST = ["cinematic_dramatic.mp3", "my_office.mp3"]

# Ads code
REWARD_INTERSTITIAL = "ca-app-pub-2909842258525517/6684743133"
INTERSTITIAL = "ca-app-pub-2909842258525517/7085343595"
