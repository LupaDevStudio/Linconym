"""
Module to store all the paths used for the app files and folders
"""

###############
### Imports ###
###############

from kivy.utils import platform

#################
### Constants ###
#################

MOBILE_MODE = platform == "android"

if MOBILE_MODE:
    from android.storage import app_storage_path  # pylint: disable=import-error # type: ignore
    PATH_APP_FOLDER = app_storage_path() + "/"
else:
    PATH_APP_FOLDER = "./"

# Path for the folders
PATH_RESOURCES_FOLDER = "resources/"

# Path for the user data
PATH_USER_DATA = PATH_APP_FOLDER + "data.json"

# Path for the screen
PATH_SCREENS = "screens/"

# Path for the resources
PATH_IMAGES = PATH_RESOURCES_FOLDER + "images/"
PATH_TEMP_IMAGES = PATH_IMAGES + "temp/"
PATH_BACKGROUNDS = PATH_IMAGES + "backgrounds/"
PATH_BADGES = PATH_IMAGES + "badges/"
PATH_SOUNDS = PATH_RESOURCES_FOLDER + "sounds/"
PATH_MUSICS = PATH_RESOURCES_FOLDER + "musics/"
PATH_FONTS = PATH_RESOURCES_FOLDER + "fonts/"
PATH_GAMEPLAY = PATH_RESOURCES_FOLDER + "gameplay.json"
PATH_THEMES = PATH_RESOURCES_FOLDER + "themes.json"
PATH_WORDS_375K = PATH_RESOURCES_FOLDER + "english_words_375k.txt"
PATH_WORDS_10K = PATH_RESOURCES_FOLDER + "english_words_10k.txt"
PATH_WORDS_34K = PATH_RESOURCES_FOLDER + "english_words_34k.txt"
PATH_WORDS_88K = PATH_RESOURCES_FOLDER + "english_words_88k.txt"

# Path for the fonts
PATH_TEXT_FONT = PATH_FONTS + "Oxanium-Bold.ttf"
PATH_TITLE_FONT = PATH_FONTS + "Oxanium-ExtraBold.ttf"
