"""
Module to create the act button.
"""

###############
### Imports ###
###############

### Kivy imports ###

from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import (
    StringProperty,
    NumericProperty,
    ColorProperty,
    BooleanProperty,
    ObjectProperty
)

### Local imports ###

from tools.path import (
    PATH_TEXT_FONT
)
from tools.constants import (
    CUSTOM_BUTTON_BACKGROUND_COLOR,
    MUSICS_DICT,
    LABEL_FONT_SIZE,
    OPACITY_ON_BUTTON_PRESS
)

#############
### Class ###
#############


class MusicLayout(ButtonBehavior, RelativeLayout):
    """
    The music layout with a white round rectangle background.
    It is composed of a play/pause button on the left, a title.
    It can all be comprised of a buy/select button on the right.
    """

    background_color = CUSTOM_BUTTON_BACKGROUND_COLOR
    music_key = StringProperty()
    music_title = StringProperty()
    music_price = NumericProperty()
    font_size = NumericProperty(LABEL_FONT_SIZE)
    font_ratio = NumericProperty(1)
    text_font_name = StringProperty(PATH_TEXT_FONT)
    primary_color = ColorProperty((1, 1, 1, 1))
    radius = NumericProperty(40)
    is_playing = BooleanProperty(False)
    has_bought_music = BooleanProperty(False)
    is_using_music = BooleanProperty(False)
    release_function = ObjectProperty()
    disable_button = BooleanProperty(False)

    def __init__(
            self,
            music_key: str = "",
            release_function=lambda: 1 + 1,
            font_ratio=None,
            **kwargs):

        if font_ratio is not None:
            self.font_ratio = font_ratio

        self.release_function = release_function
        self.always_release = True

        self.music_title = MUSICS_DICT[music_key]["name"]
        self.music_price = MUSICS_DICT[music_key]["price"]

        super().__init__(**kwargs)

    def update_display(self):
        if self.has_bought_music:
            try:
                self.remove_widget(self.ids.buy_music_button)
            except:
                pass
            self.ids.select_music_button.opacity = 1
            self.ids.select_music_button.disable_button = False
        else:
            self.ids.buy_music_button.opacity = 1
            self.ids.buy_music_button.disable_button = False
            self.ids.select_music_button.opacity = 0
            self.ids.select_music_button.disable_button = True

    def disable_buy_select(self):
        """
        Disable the right part of the layout (for the credits screen).
        
        Parameters
        ----------
        None
        
        Returns
        -------
        None
        """
        self.remove_widget(self.ids.buy_music_button)
        self.remove_widget(self.ids.select_music_button)

    def play_sound(self):
        if self.is_playing:
            # TODO play the former music
            self.is_playing = False
        else:
            # TODO play the new music
            self.is_playing = True

    def buy_music(self):
        print("Buy music")
        self.has_bought_music = True
        self.update_display()

    def choose_music(self):
        # TODO change the checks and update the music
        self.is_using_music = True

    def on_press(self):
        if not self.disable_button:
            self.opacity = OPACITY_ON_BUTTON_PRESS

    def on_release(self):
        if not self.disable_button:
            self.release_function()
            self.opacity = 1
