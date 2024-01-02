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
    THEMES_DICT,
    DICT_AMOUNT_ADS,
    DICT_AMOUNT_BUY
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
        current_theme_colors = USER_DATA.settings["current_theme_colors"]
        self.primary_color = THEMES_DICT[current_theme_colors]["primary"]
        self.secondary_color = THEMES_DICT[current_theme_colors]["secondary"]
        self.set_back_image_path(
            PATH_BACKGROUNDS + THEMES_DICT[current_theme_image]["image"])
        self.build_list_ads()
        self.build_list_buy()
        return super().on_enter(*args)

    def go_backwards(self):
        self.manager.current = self.former_screen

    def build_list_ads(self):
        self.list_ads = []
        for ad in USER_DATA.ads:
            if USER_DATA.ads[ad]:
                self.list_ads.append({
                    "color": self.secondary_color,
                    "disable_button": True,
                    "amount": DICT_AMOUNT_ADS[ad]
                })
            else:
                self.list_ads.append({
                    "color": self.primary_color,
                    "disable_button": False,
                    "amount": DICT_AMOUNT_ADS[ad]
                })

    def build_list_buy(self):
        self.list_buy = []
        for counter in range(1, 4):
            self.list_buy.append({
                "color": self.primary_color,
                "disable_button": False,
                "amount": DICT_AMOUNT_BUY[str(counter)]["amount"],
                "price": DICT_AMOUNT_BUY[str(counter)]["price"]
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
        USER_DATA.change_boosters(number)
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
        pass
