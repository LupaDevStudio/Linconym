"""
Package to manage the screens of the application
"""

###############
### Imports ###
###############

# Import the custom widgets
from screens.custom_widgets import (
    BottomBar,
    CustomButton,
    ThreeStars,
    SideImageButton,
    RoundedButtonImage,
    ExperienceCounter,
    CircleIconButton,
    RoundButton,
    BoosterLayout
)

# Import the screens
from screens.home import HomeScreen
from screens.profile import ProfileScreen
from screens.customization import CustomizationScreen
from screens.settings import SettingsScreen
from screens.classic_mode import ClassicModeScreen
from screens.boosters import BoostersScreen
