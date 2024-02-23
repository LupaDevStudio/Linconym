"""
Module to create the settings screen.
"""

###############
### Imports ###
###############

### Python imports ###

import os
import random
import webbrowser

### Kivy imports ###

from kivy.properties import StringProperty

### Local imports ###

from tools.constants import (
    USER_DATA,
    THEMES_DICT,
    __version__,
    SCREEN_TITLE,
    SCREEN_BOTTOM_BAR
)
from tools.kivy_tools import (
    LinconymScreen
)
from tools.path import (
    PATH_TEMP_IMAGES
)
from tools.generate_texture import (
    generate_spinner_texture,
    convert_1_to_255
)
from tools import (
    music_mixer,
    sound_mixer
)

#############
### Class ###
#############


class SettingsScreen(LinconymScreen):
    """
    Class to manage the settings screen.
    """

    dict_type_screen = {
        SCREEN_TITLE : "Settings",
        SCREEN_BOTTOM_BAR : "settings"
    }
    version_text = StringProperty()

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.version_text = "Version " + str(__version__)
        self.ids.sound_slider.bind(value=self.update_sound_volume)
        self.ids.music_slider.bind(value=self.update_music_volume)

    def on_pre_enter(self, *args):
        current_theme_color = USER_DATA.settings["current_theme_colors"]
        current_primary_color = tuple(
            map(convert_1_to_255, THEMES_DICT[current_theme_color]["primary"]))
        current_secondary_color = tuple(
            map(convert_1_to_255, THEMES_DICT[current_theme_color]["secondary"]))
        current_save_int = random.randint(0, 1e9)
        self.save_int = current_save_int
        generate_spinner_texture(primary_color=current_primary_color,
                                 secondary_color=current_secondary_color,
                                 save_int=current_save_int)
        self.ids["sound_slider"].update_textures(save_int=current_save_int)
        self.ids["music_slider"].update_textures(save_int=current_save_int)
        return super().on_pre_enter(*args)

    def on_leave(self, *args):
        USER_DATA.save_changes()
        os.remove(PATH_TEMP_IMAGES + f"circle_{self.save_int}.png")
        os.remove(PATH_TEMP_IMAGES + f"rectangle_{self.save_int}.png")
        return super().on_leave(*args)

    def update_sound_volume(self, widget, value):
        sound_volume = value
        sound_mixer.change_volume(sound_volume)
        USER_DATA.settings["sound_volume"] = sound_volume

    def update_music_volume(self, widget, value):
        music_volume = value
        music_mixer.change_volume(music_volume)
        USER_DATA.settings["music_volume"] = music_volume

    def open_credits(self):
        self.manager.go_to_next_screen("credits")

    def open_lupa_website(self):
        """
        Open LupaDevStudio website.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        webbrowser.open("https://lupadevstudio.com", 2)
