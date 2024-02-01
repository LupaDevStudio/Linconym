"""
Module to create the themes screen.
"""

###############
### Imports ###
###############

### Kivy imports ###

from kivy.clock import Clock

from kivy.properties import (
    NumericProperty,
    ColorProperty
)

### Local imports ###

from tools.path import (
    PATH_BACKGROUNDS
)
from tools.constants import (
    USER_DATA,
    THEMES_DICT,
    FPS
)
from tools.kivy_tools import (
    ImprovedScreen
)
from screens.custom_widgets import (
    ThemeLayout
)


#############
### Class ###
#############


class ThemesScreen(ImprovedScreen):
    """
    Class to manage the themes screen.
    """

    coins_count = NumericProperty()
    primary_color = ColorProperty((0, 0, 0, 1))
    secondary_color = ColorProperty((0, 0, 0, 1))

    def __init__(self, **kwargs) -> None:
        current_theme_image = USER_DATA.settings["current_theme_image"]
        super().__init__(
            back_image_path=PATH_BACKGROUNDS +
            THEMES_DICT[current_theme_image]["image"],
            **kwargs)
        self.THEME_LAYOUT_DICT = {}
        self.on_resize()
        self.fill_scrollview()

    def on_pre_enter(self, *args):
        self.coins_count = USER_DATA.user_profile["coins"]
        current_theme_colors = USER_DATA.settings["current_theme_colors"]
        self.primary_color = THEMES_DICT[current_theme_colors]["primary"]
        self.secondary_color = THEMES_DICT[current_theme_colors]["secondary"]
        return super().on_pre_enter(*args)

    def on_resize(self, *args):
        for act in self.THEME_LAYOUT_DICT:
            self.THEME_LAYOUT_DICT[act].font_ratio = self.font_ratio
        return super().on_resize(*args)

    def go_backwards(self):
        self.manager.go_to_previous_screen()

    def go_to_boosters(self):
        self.manager.go_to_next_screen(
            next_screen_name="boosters"
        )

    def update_coins(self):
        self.coins_count = USER_DATA.user_profile["coins"]

    def update_theme_layouts_display(self):
        """
        Update all theme widgets.
        """
        for theme in self.THEME_LAYOUT_DICT:
            self.THEME_LAYOUT_DICT[theme].update_display()

        current_theme_image = USER_DATA.settings["current_theme_image"]
        new_image = THEMES_DICT[current_theme_image]["image"]

        current_theme_colors = USER_DATA.settings["current_theme_colors"]
        self.primary_color = THEMES_DICT[current_theme_colors]["primary"]

        if (self.back_image_path != PATH_BACKGROUNDS + new_image and self.opacity_state == "main") \
                or (self.second_back_image_path != PATH_BACKGROUNDS + new_image and self.opacity_state == "second"):
            # Change the background image smoothly for this screen
            self.change_background(new_image)

            # Change the background image for all screens except this one
            self.manager.change_all_background_images(
                PATH_BACKGROUNDS + new_image)

    def change_background(self, new_image: str):
        """
        Change smoothly of background image.

        Parameters
        ----------
        new_image : str
            Name of the new image to set as background.

        Returns
        -------
        None
        """
        # Change the image of the background
        if self.opacity_state == "main":
            self.set_back_image_path(
                back_image_path=PATH_BACKGROUNDS + new_image,
                mode="second"
            )
        elif self.opacity_state == "second":
            self.set_back_image_path(
                back_image_path=PATH_BACKGROUNDS + new_image,
                mode="main"
            )

        # Schedule the change of the opacity to have a smooth transition
        Clock.schedule_interval(self.change_background_opacity, 1 / FPS)

    def fill_scrollview(self):
        scrollview_layout = self.ids["scrollview_layout"]
        # Load the widgets
        self.THEME_LAYOUT_DICT = {}
        for theme in THEMES_DICT:
            current_theme_button = ThemeLayout(
                theme_key=theme,
                source=PATH_BACKGROUNDS + THEMES_DICT[theme]["image"],
                font_ratio=self.font_ratio * 0.8)
            current_theme_button.update_display()
            self.THEME_LAYOUT_DICT[theme] = current_theme_button
            scrollview_layout.add_widget(self.THEME_LAYOUT_DICT[theme])
