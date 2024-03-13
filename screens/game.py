"""
Module to create the game screen.
"""

###############
### Imports ###
###############

### Python imports ###

from functools import partial
from typing import Literal

### Kivy imports ###

from kivy.properties import (
    StringProperty,
    NumericProperty
)

### Local imports ###

from tools.constants import (
    USER_DATA,
    LETTER_FONT_SIZE,
    SCREEN_BACK_ARROW,
    SCREEN_TUTORIAL,
    GAMEPLAY_DICT
)
from screens.custom_widgets import (
    LinconymScreen
)
from tools import (
    music_mixer
)
from screens import (
    ColoredRoundedButton
)
from tools.linconym import (
    is_valid,
    level_has_saved_data,
    Game
)
from screens.custom_widgets import TreeLayout

#############
### Class ###
#############


class GameScreen(LinconymScreen):
    """
    Class to manage the game screen.
    """

    current_level_name = StringProperty()
    dict_type_screen = {
        SCREEN_BACK_ARROW: "",
        SCREEN_TUTORIAL: ""
    }

    nb_stars = NumericProperty()
    start_word = StringProperty("boy")
    current_word = StringProperty("")
    new_word = StringProperty("")
    end_word = StringProperty("toys")
    start_to_end_label = StringProperty("")
    list_widgets_letters = []

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.current_act_id: str
        self.current_level_id: str

    def reload_kwargs(self, dict_kwargs):
        self.current_act_id = dict_kwargs["current_act_id"]
        self.current_level_id = dict_kwargs["current_level_id"]

    def on_pre_enter(self, *args):
        super().on_pre_enter(*args)

        # Store the dict containing the user progress
        self.level_saved_data = USER_DATA.classic_mode[self.current_act_id][self.current_level_id]

        # Save the dict containing the level instructions
        self.level_info = GAMEPLAY_DICT[self.current_act_id][self.current_level_id]

        # Extract start word and end word
        self.start_word = self.level_info["start_word"]
        self.end_word = self.level_info["end_word"]
        self.start_to_end_label = (
            self.start_word + " > " + self.end_word).upper()

        # Load the save data if some are provided
        if level_has_saved_data(self.level_saved_data):
            current_position = self.level_saved_data["current_position"]
            words_found = self.level_saved_data["words_found"]
            position_to_word_id = self.level_saved_data["position_to_word_id"]
        else:
            current_position = "0"
            words_found = [self.start_word]
            position_to_word_id = {"0": 0}

        # Create a game instance
        game = Game(
            start_word=self.start_word,
            end_word=self.end_word,
            current_position=current_position,
            words_found=words_found,
            position_to_word_id=position_to_word_id)

        self.transparent_secondary_color = [
            self.secondary_color[0], self.secondary_color[1], self.secondary_color[2], 0.3]
        self.ids.keyboard_layout.build_keyboard()

        self.nb_stars = USER_DATA.classic_mode[self.current_act_id][self.current_level_id]["nb_stars"]

        # Build the tree with the saved data
        self.ids["tree_layout"].build_layout(
            position_to_word_id=position_to_word_id,
            words_found=words_found,
            current_position=current_position)

        temp = self.current_act_id.replace("Act", "")
        self.current_level_name = "Act " + temp + " – " + self.current_level_id
        self.load_game_play()
        self.load_game_user()
        self.build_word()
        self.check_disable_keyboard()
        self.check_enable_submit_button()

    def on_pre_leave(self, *args):
        self.ids.keyboard_layout.destroy_keyboard()

        return super().on_leave(*args)

    def check_disable_keyboard(self):

        # Disable the back button if we have nothing to delete
        if len(self.new_word) == 0:
            self.ids.keyboard_layout.disable_delete_button()
        else:
            self.ids.keyboard_layout.activate_delete_button()

        # Disable the letters is the word is already filled
        if len(self.new_word) >= len(self.current_word) + 1:
            self.ids.keyboard_layout.disable_letters()
        else:
            self.ids.keyboard_layout.activate_letters()

    def check_enable_submit_button(self):
        """
        Enable the submit button if the word entered is valid.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        if is_valid(
                new_word=self.new_word.lower(),
                current_word=self.current_word.lower()):
            self.enable_submit_button()
        else:
            self.disable_submit_button()

    def touch_letter(self, letter):
        """
        React when a letter of the keyboard is released.

        Parameters
        ----------
        letter : str
            Letter pressed. Can be any letter in capital or "DELETE".

        Returns
        -------
        None
        """
        # Delete the last letter of the current word
        if letter == "DELETE":
            self.new_word = self.new_word[:-1]

        # Add the new letter to the current word
        else:
            self.new_word += letter

        # Disable/Enable the keyboard and the submit button in consequence
        self.check_disable_keyboard()
        self.check_enable_submit_button()

        # Rebuild the display of the word
        self.build_word()

    def build_word(self):
        x_center = 0.5
        number_mandatory_letters = len(self.current_word) - 1
        number_letters = number_mandatory_letters + 2
        next_letter_counter = len(self.new_word)
        horizontal_padding = 0.02
        size_letter = 0.07
        height_letter = 0.05
        margin_left = 0

        # Adapt the size of the letters if there are too many
        if number_letters >= 11:
            size_letter = (0.95 - (number_letters - 1) *
                           horizontal_padding) / number_letters
            margin_left = 0.025

        # Remove the previous widgets
        for letter_widget in self.list_widgets_letters:
            self.remove_widget(letter_widget)

        # Create the letters
        for counter_letter in range(number_letters):

            # Determine the color of the outline
            if counter_letter == next_letter_counter:
                outline_color = self.primary_color
            else:
                if counter_letter >= number_mandatory_letters:
                    outline_color = self.transparent_secondary_color
                else:
                    outline_color = self.secondary_color

            # Determine the content of the letter
            try:
                letter = self.new_word[counter_letter]
            except:
                letter = ""

            # Determine the x position of the letter
            if number_letters % 2 == 0:
                x_position = margin_left + x_center + \
                    (counter_letter - number_letters / 2 + 0.5) * horizontal_padding + \
                    (counter_letter - number_letters / 2) * size_letter
            else:
                x_position = margin_left + x_center + (counter_letter - number_letters / 2) * size_letter + (
                    counter_letter - number_letters / 2 - 0.5) * horizontal_padding

            # Create the letter widget
            letter_widget = ColoredRoundedButton(
                text=letter,
                background_color=(1, 1, 1, 1),
                pos_hint={"x": x_position, "y": 0.275},
                font_size=LETTER_FONT_SIZE,
                font_ratio=self.font_ratio,
                size_hint=(size_letter, height_letter),
                color_label=(0, 0, 0, 1),
                outline_color=outline_color,
                disable_button=True
            )

            self.add_widget(letter_widget)
            self.list_widgets_letters.append(letter_widget)

    def load_game_play(self):
        pass

    def load_game_user(self):
        pass

    def submit_word(self):
        print("TODO rajouter le nouveau mot dans l'arbre. Ce nouveau mot est forcément valide (on le sait), cela a déjà été vérifié avec la présence ou non du submit button.")

        # Change the current and new word
        if not self.check_level_complete():
            self.current_word = self.new_word
            self.new_word = ""

            # Enable the keyboard and disable the submit button
            self.build_word()
            self.check_disable_keyboard()
            self.check_enable_submit_button()

    def check_level_complete(self):
        # The level is complete
        if self.new_word == self.end_word:
            print("TODO YOU WIN afficher la popup")
            self.current_word = self.start_word
            self.ids.keyboard_layout.disable_whole_keyboard()
            self.disable_submit_button()
            return True
        return False

    def enable_submit_button(self):
        # self.ids.submit_button.opacity = 1
        self.ids.submit_button.disable_button = False

    def disable_submit_button(self):
        # self.ids.submit_button.opacity = 0
        self.ids.submit_button.disable_button = True

    def go_to_quests_screen(self):
        dict_kwargs = {
            "current_level_id": self.current_level_id,
            "current_act_id": self.current_act_id
        }
        self.go_to_next_screen(
            screen_name="quests",
            current_dict_kwargs=dict_kwargs,
            next_dict_kwargs=dict_kwargs)

    def go_to_configure_tree_screen(self):
        dict_kwargs = {
            "current_level_id": self.current_level_id,
            "current_act_id": self.current_act_id
        }
        self.go_to_next_screen(
            screen_name="configure_tree",
            current_dict_kwargs=dict_kwargs,
            next_dict_kwargs=dict_kwargs)
