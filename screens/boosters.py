"""
Module to create the profile screen.
"""

###############
### Imports ###
###############

### Kivy imports ###

from kivy.properties import (
    ColorProperty,
    NumericProperty,
    StringProperty,
    ListProperty
)

### Local imports ###

from tools.path import (
    PATH_BACKGROUNDS    
)
from tools.constants import (
    USER_DATA,
    THEMES_DICT
)
from tools.kivy_tools import (
    ImprovedScreen
)


#############
### Class ###
#############


class BoostersScreen(ImprovedScreen):
    """
    Class to manage the screen with the coins boosters.
    """

    coins_count = NumericProperty()
    primary_color = ColorProperty((0, 0, 0, 1))
    secondary_color = ColorProperty((0, 0, 0, 1))
    former_screen = StringProperty()
    list_ads = ListProperty()
    list_buy = ListProperty()

    def __init__(self, **kwargs) -> None:
        current_theme_image = USER_DATA.settings["current_theme_image"]
        super().__init__(
            back_image_path=PATH_BACKGROUNDS +
            THEMES_DICT[current_theme_image]["image"],
            **kwargs)

    def on_enter(self, *args):
        self.coins_count = USER_DATA.user_profile["coins"]
        current_theme_image = USER_DATA.settings["current_theme_image"]
        self.primary_color = THEMES_DICT[current_theme_image]["primary"]
        self.secondary_color = THEMES_DICT[current_theme_image]["secondary"]
        self.set_back_image_path(
            PATH_BACKGROUNDS + THEMES_DICT[current_theme_image]["image"])
        self.build_list_ads()
        self.build_list_buy()
        return super().on_enter(*args)

    def go_backwards(self):
        self.manager.current = self.former_screen

    def build_list_ads(self):
        self.list_ads = {}
        for ad in USER_DATA.boosters["dict_ads"]:
            if USER_DATA.boosters["dict_ads"][ad]:
                self.list_ads.append({
                    "color": self.secondary_color,
                    "disable_button": True
                })
            else:
                self.list_ads.append({
                    "color": self.primary_color,
                    "disable_button": False
                })

    def build_list_buy(self):
        for buy in USER_DATA.boosters["dict_buy"]:
            if USER_DATA.boosters["dict_buy"][buy]:
                self.list_buy.append({
                    "color": self.secondary_color,
                    "disable_button": True
                })
            else:
                self.list_buy.append({
                    "color": self.primary_color,
                    "disable_button": False
                })

    def see_ad(self, number: int):
        """
        Launch the ad and update the display.
        
        Parameters
        ----------
        number : int
            Number of the ad to watch
        
        Returns
        -------
        None
        """
        USER_DATA.change_boosters("ads", number)
        self.build_list_ads()

    def buy_booster(self, number: int):
        """
        Buy a booster and update the display.
        
        Parameters
        ----------
        number : int
            Number of the booster to buy
        
        Returns
        -------
        None
        """
        USER_DATA.change_boosters("buy", number)
        self.build_list_buy()
