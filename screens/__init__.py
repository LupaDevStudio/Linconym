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
    BoosterLayout,
    ColoredRoundedButton,
    KeyboardLayout,
    ColoredRoundedButtonImage,
    MusicLayout
)

# Import the screens
from screens.home import HomeScreen
from screens.profile import ProfileScreen
from screens.themes import ThemesScreen
from screens.settings import SettingsScreen
from screens.classic_mode import ClassicModeScreen
from screens.boosters import BoostersScreen
from screens.levels import LevelsScreen
from screens.customization import CustomizationScreen
from screens.game import GameScreen
from screens.quests import QuestsScreen
from screens.credits import CreditsScreen
from screens.preview import PreviewScreen
from screens.musics import MusicsScreen
from screens.configure_tree import ConfigureTreeScreen
from screens.achievements import AchievementsScreen
