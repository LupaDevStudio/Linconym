"""
Module to create the settings screen.
"""

###############
### Imports ###
###############

### Python imports ###

import os
import random

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
    PATH_BACKGROUNDS,
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
from screens.custom_widgets import CustomSlider

#############
### Class ###
#############


class SettingsScreen(ImprovedScreen):
    """
    Class to manage the settings screen.
    """

    version_text = StringProperty()

    # def add_sliders(self):
    #     self.sound_slider = CustomSlider(
    #         min=0,
    #         max=1,
    #         value=USER_DATA.settings["sound_volume"],
    #         size_hint=(0.7, 0.06),
    #         pos_hint={"center_x": 0.5, "center_y": 0.59})
    #     self.add_widget(self.sound_slider)
    #     self.sound_slider.bind(value=self.update_sound_volume)
    #     self.music_slider = CustomSlider(
    #         min=0,
    #         max=1,
    #         value=USER_DATA.settings["sound_volume"],
    #         size_hint=(0.7, 0.06),
    #         pos_hint={"center_x": 0.5, "center_y": 0.59})
    #     self.add_widget(self.music_slider)
    #     self.music_slider.bind(value=self.update_music_volume)

    # def destroy_sliders(self):
    #     self.remove_widget(self.sound_slider)
    #     self.remove_widget(self.music_slider)

    def __init__(self, **kwargs) -> None:
        current_theme_image = USER_DATA.settings["current_theme_image"]
        self.version_text = "Version " + str(__version__)
        super().__init__(
            back_image_path=PATH_BACKGROUNDS +
            THEMES_DICT[current_theme_image]["image"],
            **kwargs)
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

    def on_enter(self, *args):
        current_theme_image = USER_DATA.settings["current_theme_image"]
        self.set_back_image_path(
            PATH_BACKGROUNDS + THEMES_DICT[current_theme_image]["image"])
        return super().on_enter(*args)

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
