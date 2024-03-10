"""
Module to create an improved kivy screen for Linconym.
"""

###############
### Imports ###
###############

### Kivy imports ###

from kivy.properties import (
    StringProperty,
    ColorProperty
)

### Local imports ###

from tools.kivy_tools import ImprovedScreen
from tools.constants import (
    USER_DATA,
    THEMES_DICT,
    SCREEN_TITLE,
    SCREEN_BOTTOM_BAR,
    SCREEN_BACK_ARROW,
    SCREEN_TUTORIAL,
    TUTORIAL
)
from tools.path import (
    PATH_BACKGROUNDS
)
from screens.custom_widgets.popup.tutorial_popup import (
    TutorialPopup
)


class LinconymScreen(ImprovedScreen):
    """
    Improved screen class for Linconym.
    It contains the title, the back arrow and the bottom bar.
    It also contains the 
    """

    # Configuration of the main widgets
    dict_type_screen: dict = {}
    title_screen = StringProperty()
    selected_bottom_bar = StringProperty()

    # Configuration of the theme
    primary_color = ColorProperty((0, 0, 0, 1))
    secondary_color = ColorProperty((0, 0, 0, 1))

    def __init__(self, **kw):
        current_theme_image = USER_DATA.settings["current_theme_image"]
        super().__init__(
            back_image_path=PATH_BACKGROUNDS +
            THEMES_DICT[current_theme_image]["image"],
            **kw)

        current_theme_colors = USER_DATA.settings["current_theme_colors"]
        self.primary_color = THEMES_DICT[current_theme_colors]["primary"]
        self.secondary_color = THEMES_DICT[current_theme_colors]["secondary"]

        # Display the title or not
        if SCREEN_TITLE in self.dict_type_screen:
            self.title_screen = self.dict_type_screen[SCREEN_TITLE]
        else:
            self.remove_widget(self.ids.title_label)

        # Display the bottom bar or not
        if SCREEN_BOTTOM_BAR in self.dict_type_screen:
            self.selected_bottom_bar = self.dict_type_screen[SCREEN_BOTTOM_BAR]
        else:
            self.remove_widget(self.ids.bottom_bar)

        # Display the back arrow or not
        if not SCREEN_BACK_ARROW in self.dict_type_screen:
            self.remove_widget(self.ids.back_arrow)

        # Display the tutorial icon or not
        if not SCREEN_TUTORIAL in self.dict_type_screen:
            self.remove_widget(self.ids.tutorial_button)

    def on_pre_enter(self, *args):
        # current_theme_image = USER_DATA.settings["current_theme_image"]
        current_theme_colors = USER_DATA.settings["current_theme_colors"]
        self.primary_color = THEMES_DICT[current_theme_colors]["primary"]
        self.secondary_color = THEMES_DICT[current_theme_colors]["secondary"]
        # self.set_back_image_path(
        #     PATH_BACKGROUNDS + THEMES_DICT[current_theme_image]["image"])
        return super().on_pre_enter(*args)

    def open_tutorial(self, screen_name):
        popup = TutorialPopup(
            primary_color=self.primary_color,
            secondary_color=self.secondary_color,
            title=TUTORIAL[screen_name]["title"],
            tutorial_content=TUTORIAL[screen_name]["tutorial_content"],
            font_ratio=self.font_ratio)
        popup.open()
