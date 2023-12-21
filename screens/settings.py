"""
Module to create the settings screen.
"""

###############
### Imports ###
###############

### Kivy imports ###

from kivy.properties import StringProperty

### Local imports ###

from tools.constants import (
    USER_DATA,
    THEMES_DICT,
    __version__
)
from tools.kivy_tools import (
    ImprovedScreen,
)
from tools.path import (
    PATH_BACKGROUNDS
)
from tools import (
    music_mixer,
    sound_mixer
)

#############
### Class ###
#############


class SettingsScreen(ImprovedScreen):
    """
    Class to manage the settings screen.
    """

    version_text = StringProperty()

    def __init__(self, **kwargs) -> None:
        current_theme_image = USER_DATA.settings["current_theme_image"]
        self.version_text = "Version " + str(__version__)
        super().__init__(
            back_image_path=PATH_BACKGROUNDS +
            THEMES_DICT[current_theme_image]["image"],
            **kwargs)
        self.ids.sound_slider.bind(value=self.update_sound_volume)
        self.ids.music_slider.bind(value=self.update_music_volume)

    def on_enter(self, *args):
        current_theme_image = USER_DATA.settings["current_theme_image"]
        self.set_back_image_path(
            PATH_BACKGROUNDS + THEMES_DICT[current_theme_image]["image"])
        return super().on_enter(*args)

    def on_leave(self, *args):
        USER_DATA.save_changes()
        return super().on_leave(*args)

    def update_sound_volume(self, widget, value):
        sound_volume = value
        sound_mixer.change_volume(sound_volume)
        USER_DATA.settings["sound_volume"] = sound_volume

    def update_music_volume(self, widget, value):
        music_volume = value
        music_mixer.change_volume(music_volume)
        USER_DATA.settings["music_volume"] = music_volume
