"""
Main module of Linconym.
"""


###############
### Imports ###
###############

### Python imports ###
import os

### Kivy imports ###

# Disable back arrow
from kivy.config import Config
Config.set('kivy', 'exit_on_escape', '0')

from kivy.app import App
from kivy.uix.screenmanager import (
    ScreenManager,
    NoTransition,
    Screen
)
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.clock import Clock

### Local imports ###

from tools.path import (
    PATH_IMAGES,
    PATH_TEMP_IMAGES
)
from tools.constants import (
    MOBILE_MODE,
    FPS,
    MSAA_LEVEL
)
import screens.opening


###############
### General ###
###############


class WindowManager(ScreenManager):
    """
    Screen manager, which allows the navigation between the different menus.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.transition = NoTransition()
        self.list_former_screens = []
        current_screen = Screen(name="temp")
        self.add_widget(current_screen)
        self.current = "temp"

    def change_all_background_images(self, new_image_path):
        for screen_name in self.screen_names:
            if screen_name != "temp" and screen_name != "customization":
                screen = self.get_screen(screen_name)
                screen.set_back_image_path(new_image_path)


class MainApp(App, Widget):
    """
    Main class of the application.
    """

    def build_config(self, config):
        """
        Build the config file for the application.

        It sets the FPS number and the antialiasing level.
        """
        config.setdefaults('graphics', {
            'maxfps': str(FPS),
            'multisamples': str(MSAA_LEVEL)
        })

    def build(self):
        """
        Build the application.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        Window.clearcolor = (0, 0, 0, 1)
        self.icon = PATH_IMAGES + "logo.png"

    def on_resume(self):
        current_screen_name = self.root_window.children[0].current
        self.root_window.children[0].get_screen(current_screen_name).refresh()
        return super().on_resume()

    def on_stop(self):
        temp_images_list = os.listdir(PATH_TEMP_IMAGES)
        for temp_image in temp_images_list:
            if temp_image.endswith(".png"):
                os.remove(PATH_TEMP_IMAGES + temp_image)
        return super().on_stop()

    def on_start(self):
        if MOBILE_MODE:
            Window.update_viewport()

        # Open the opening screen
        opening_screen = screens.opening.OpeningScreen(name="opening")
        self.root_window.children[0].add_widget(opening_screen)
        self.root_window.children[0].current = "opening"

        Clock.schedule_once(
            self.root_window.children[0].get_screen("opening").launch_thread)

        print("Main app started")

        return super().on_start()


# Run the application
if __name__ == "__main__":
    Window.size = (480, 854)
    MainApp().run()
