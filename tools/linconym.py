"""
Module containing the core of Linconym.
"""

###############
### Imports ###
###############

from tools.path import (
    PATH_GAMEPLAY,
    PATH_RESOURCES_FOLDER
)
from tools.constants import (
    ENGLISH_WORDS_DICTS,
    GAMEPLAY_DICT,
    USER_DATA,
    XP_PER_LEVEL
)
from tools.basic_tools import (
    dichotomy,
    save_json_file,
    load_json_file
)

#################
### Functions ###
#################


def is_in_english_words(word: str) -> bool:
    """
    Indicates whether a word belongs to the english words dictionnary or not.

    Parameters
    ----------
    word : str
        Word to check.

    Returns
    -------
    bool
        True if the word is in the dictionnary, False otherwise.
    """

    return dichotomy(word, ENGLISH_WORDS_DICTS["375k"]) is not None


def count_different_letters(word1: str, word2: str) -> int:
    """
    Count the number of different letters between two words.

    Parameters
    ----------
    word1 : str
        First word.
    word2 : str
        Second word.

    Returns
    -------
    int
        Number of different letters.
    """

    # Initialise the number of different letters
    nb_different_letters = 0
    used_letters = [False] * len(word2)

    # Iterate over the letters of the first word
    for letter in word1:
        valid_letter_bool = False
        for i, check_letter in enumerate(word2):
            if check_letter == letter and used_letters[i] is False:
                used_letters[i] = True
                valid_letter_bool = True
                break
        if valid_letter_bool is False:
            nb_different_letters += 1

    return nb_different_letters


def count_common_letters(word1: str, word2: str) -> int:
    res = len(word1) - count_different_letters(word1, word2)
    # TEMP
    res += (len(word2) - len(word1)) // 2
    if res < 0:
        res = 0
    return res


def is_valid(new_word: str, current_word: str, skip_in_english_words: bool = False) -> bool:
    """
    Determine whether a word is valid or not to be submitted.

    Parameters
    ----------
    new_word : str
        New word to check.
    current_word : str
        Current word.
    skip_in_english_words : bool = False
        If True, a word doesn't need to be in any dictionary to be valid (i.e., in_english_words() is not called here).

    Returns
    -------
    bool
        True if the word is valid, False otherwise.
    """

    # Check if the new word derives from the current word
    if len(new_word) - len(current_word) == 0:
        # Shuffle and change one letter case
        if count_different_letters(new_word, current_word) <= 1:
            derive_bool = True
        else:
            derive_bool = False
    elif len(new_word) - len(current_word) == 1:
        # New letter addition case
        if count_different_letters(new_word, current_word) <= 1:
            derive_bool = True
        else:
            derive_bool = False
    elif len(new_word) - len(current_word) == -1:
        # Letter deletion case
        if count_different_letters(new_word, current_word) == 0:
            derive_bool = True
        else:
            derive_bool = False
    else:
        derive_bool = False

    # Check if the new word is in the english dictionnary
    if skip_in_english_words:
        english_words_bool = True
    else:
        english_words_bool = is_in_english_words(new_word)

    # Check if the new word verifies both conditions
    valid_bool = derive_bool and english_words_bool

    return valid_bool


def find_all_next_words(current_word: str, english_words):
    next_words = []
    for word in english_words:
        if is_valid(word, current_word, skip_in_english_words=True):
            next_words.append(word)

    return next_words


def convert_position_to_wordlist(position: str, position_to_word_id, words_found):
    wordlist = []
    for i in range(1, len(position) + 1):
        word = words_found[position_to_word_id[position[:i]]]
        wordlist.append(word)
    return wordlist


def find_solutions(start_word: str, end_word: str, english_words: list = ENGLISH_WORDS_DICTS["375k"]):
    """
    Find solutions for the given start and end words by using a score based on proximity to the end word.

    Parameters
    ----------
    start_word : str
        Start word.
    end_word : str
        End word.
    english_words : list, optional
        Database to use to create the path, by default ENGLISH_WORDS_DICTS["375k"]

    Returns
    -------
    list
        Path between the two words.
    """

    start_position = (0,)
    position_to_word_id = {start_position: 0}
    words_found = [start_word]
    pile = {}

    for i in range(len(end_word) + 1):
        pile[i] = []

    pile[0].append(start_position)

    not_found = True

    while not_found:
        current_position = None
        for i in sorted(pile.keys()):
            if len(pile[i]) > 0:
                # print(i)
                current_position = pile[i].pop(0)
                break

        if current_position is None:
            return None

        current_word = words_found[position_to_word_id[current_position]]
        # print(current_word, i)
        # print(current_position)
        next_words = find_all_next_words(current_word, english_words)
        # print(len(next_words))
        new_word_id = 0

        for word in next_words:
            if word not in words_found or word == end_word:
                temp_nb_common_letters = count_common_letters(word, end_word)
                new_position = current_position + (new_word_id,)
                position_to_word_id[new_position] = len(words_found)
                words_found.append(word)
                new_word_id += 1
                if word == end_word:
                    not_found = False
                    final_position = new_position
                    print(convert_position_to_wordlist(
                        final_position, position_to_word_id, words_found))
                else:
                    pile_id = -temp_nb_common_letters + len(new_position)
                    # print(pile_id)
                    if pile_id in pile:
                        pile[pile_id].append(new_position)
                    else:
                        pile[pile_id] = [new_position]

    solution = []
    for i in range(1, len(final_position) + 1):
        word = words_found[position_to_word_id[final_position[:i]]]
        solution.append(word)

    return solution


def fill_daily_games_with_solutions():
    """
    Fill all the empty lines of the daily games json with the solutions.
    """
    DAILY_DICT = load_json_file(PATH_RESOURCES_FOLDER + "daily_games.json")
    for date in DAILY_DICT:
        start_word = DAILY_DICT[date]["start_word"]
        end_word = DAILY_DICT[date]["end_word"]
        if "simplest_solution" not in date:
            for resolution in ENGLISH_WORDS_DICTS:
                solution = find_solutions(
                    start_word=start_word,
                    end_word=end_word,
                    english_words=ENGLISH_WORDS_DICTS[resolution])
                if solution is not None:
                    DAILY_DICT[date]["simplest_solution"] = solution
                    break
        if "best_solution" not in date:
            if resolution != "375k":
                solution = find_solutions(
                    start_word=start_word,
                    end_word=end_word,
                    english_words=ENGLISH_WORDS_DICTS["375k"])
            DAILY_DICT[date]["best_solution"] = solution
    save_json_file(PATH_RESOURCES_FOLDER + "daily_games.json", DAILY_DICT)


def fill_gameplay_dict_with_solutions():
    """
    Fill all the empty lines of the gameplay dict with the solutions.
    """
    for act in GAMEPLAY_DICT:
        for level in GAMEPLAY_DICT[act]:
            if level == "name":
                continue
            start_word = GAMEPLAY_DICT[act][level]["start_word"]
            end_word = GAMEPLAY_DICT[act][level]["end_word"]
            for resolution in ENGLISH_WORDS_DICTS:
                if f"{resolution}_sol" not in GAMEPLAY_DICT[act][level]:
                    print(resolution)
                    solution = find_solutions(
                        start_word=start_word,
                        end_word=end_word,
                        english_words=ENGLISH_WORDS_DICTS[resolution])
                    if solution is not None:
                        GAMEPLAY_DICT[act][level][f"{resolution}_sol"] = len(
                            solution)
                    else:
                        GAMEPLAY_DICT[act][level][f"{resolution}_sol"] = None

    save_json_file(PATH_GAMEPLAY, GAMEPLAY_DICT)

#############
### Class ###
#############


class Game():
    """
    Class to manage all actions and variables during a game of Linconym.
    Its member variables represent a tree of words, the root of which is the start word of the game.
    Its member variables also include a cursor "pointing" to one node in particular: new words submitted by the user
    may be added as children of the node "pointed to" by this cursor if they are valid successors.
    """

    def __init__(self, start_word: str, end_word: str, quest_word: str = None, act_name: str = "Act1", lvl_name: str = "1") -> None:
        self.start_word: str = start_word
        self.end_word: str = end_word
        self.quest_word: str = quest_word
        self.act_name = act_name
        self.lvl_name = lvl_name
        self.current_position: str = "0" # Positions are strings of comma-separated integers which indicate a path in the nodes
        self.position_to_word_id = {self.current_position: 0} # A dictionary to map a (str) position to the index of its word in the words_found list[str]
        self.words_found: list[str] = [start_word]
        self.current_word: str = start_word

    def get_word(self, position: str) -> str:
        """
        Get the word at given position.

        Parameters
        ----------
        position : str
            Position to use.

        Returns
        -------
        str
            Word at given position.
        """

        return self.words_found[self.position_to_word_id[position]]
    
    def get_word_path(self, position: str) -> list[str]:
        """
        Get a list of the words forming the path to the given position.

        Parameters
        ----------
        position : str
            Position to use.

        Returns
        -------
        list[str]
            List of words leading to given position.
        """

        word_path: list[str] = []
        for i in range(len(position)):
            previous_pos: str = position[:(i+1)]
            word_path += [self.get_word(previous_pos)]
        return word_path

    def get_nb_next_words(self, position: str) -> int:
        """
        Get the number of words deriving directly from the given position.
        In tree jargon, get the number of children of the node corresponding to the input position.

        Parameters
        ----------
        position : str
            Position to use.

        Returns
        -------
        int
            Number of next words.
        """

        # Initialise the number of next words
        nb_next_words = 0

        # Iterate over all stored positions
        for key in self.position_to_word_id:
            if len(key) == len(position) + 1:
                if key[:len(position)] == position:
                    nb_next_words += 1

        return nb_next_words

    def change_position(self, new_position: str) -> None:
        """
        Change the position of the cursor from one word (node) to another.

        Parameters
        ----------
        new_position : str
            New position to set.
        """

        self.current_position = new_position
        self.current_word = self.get_word(self.current_position)
    
    def is_valid_and_new(self, new_word: str, skip_dictionary_check: bool = False) -> bool:
        """
        Checks whether a new word is absent from the WHOLE tree and is a valid successor to the current word.
        This is probably not the right method to use to check user input, because if a word is used as a part of a very long path, 
        then it cannot be used to create a shorter path anymore.

        Example: in a level asking to go from "sea" to "shell", the path "sea, seal, sell, shell" is the shortest. However, if the user already
        built the path "sea, tea, teal, seal", then they won't be able to create the shortest path anymore: all they can do is pick up from the 
        word "seal" in their already-way-too-long current path. 

        Parameters
        ----------
        new_word: str
            New word to be checked.
        skip_dictionary_check: bool = False
            If True, new_word can be valid even if it isn't in any dictionary.

        Returns
        -------
        bool
            True if new_word wasn't previously found and is valid, False otherwise.
        """

        word_is_valid: bool = is_valid(new_word, self.current_word, skip_dictionary_check)
        word_is_new: bool = not(new_word in self.words_found)
        return word_is_valid and word_is_new
    
    def is_valid_and_new_in_path(self, new_word: str, skip_dictionary_check: bool = False) -> bool:
        """
        Checks whether a new word is absent from the path leading to the current word and is a valid successor to the current word.

        Parameters
        ----------
        new_word: str
            New word to be checked.
        skip_dictionary_check: bool = False
            If True, new_word can be valid even if it isn't in any dictionary.

        Returns
        -------
        bool
            True if new_word isn't in the path leading to the current word and is valid, False otherwise.
        """

        word_is_valid: bool = is_valid(new_word, self.current_word, skip_dictionary_check)
        word_is_new_in_path: bool = not(new_word in self.get_word_path(self.current_position))
        return word_is_valid and word_is_new_in_path

    def submit_word(self, new_word: str) -> None:
        """
        Add a new word to the history if it is valid.

        Parameters
        ----------
        new_word : str
            New word to verify and add.
        """

        if self.is_valid_and_new_in_path(new_word):

            # Compute the new position
            new_word_id = self.get_nb_next_words(self.current_position)
            new_position = self.current_position + (new_word_id,)

            # Add the word to the list of words found
            self.position_to_word_id[new_position] = len(self.words_found)
            self.words_found.append(new_word)

            # Switch to the new position
            self.change_position(new_position)

            # Check if the final word is reached
            if self.current_word == self.end_word:
                print("End word reached")

        else:
            print("Word not valid")
    
    def award_stars_xp(self, nb_words_10k: int, nb_words_300k: int) -> None:
        # Only receive stars and xp if the level was completed
        if (self.current_word == self.end_word):
            solution_found: list[str] = self.get_word_path(self.current_position)

            # Stars: one for finishing the level, one for doing as good as the 10k dictionary solution, and one for doing better
            nb_stars: int = 1
            nb_words_found: int = len(solution_found)
            if (nb_words_found >= nb_words_10k):
                nb_stars += 1
            if (nb_words_found > nb_words_10k):
                nb_stars += 1
            
            # xp: get a percentage of a certain constant amount depending on proximity to the 300k dictionary solution...
            xp_fraction: float = nb_words_found / nb_words_300k
            if (xp_fraction > 1):
                xp_fraction = 1.0
            # ... and get a bonus for passing through the quest word
            quest_word_done: bool = ((self.quest_word != None) and (self.quest_word in solution_found))

            # save level progress (TEMP: only for classic mode, should probably make subclasses for classic and daily mode)
            # save stars
            STARS_KEY: str = "nb_stars"
            if (STARS_KEY in USER_DATA.classic_mode[self.act_name][self.lvl_name]):
                if (USER_DATA.classic_mode[self.act_name][self.lvl_name][STARS_KEY] < nb_stars):
                    USER_DATA.classic_mode[self.act_name][self.lvl_name][STARS_KEY] = nb_stars
            else:
                USER_DATA.classic_mode[self.act_name][self.lvl_name][STARS_KEY] = nb_stars
            # save number of words
            NB_WORDS_KEY: str = "best_solution_nb_words"
            nb_words_previous_best: int = 0
            if (NB_WORDS_KEY in USER_DATA.classic_mode[self.act_name][self.lvl_name]):
                nb_words_previous_best = USER_DATA.classic_mode[self.act_name][self.lvl_name][NB_WORDS_KEY]
                if (nb_words_previous_best < nb_words_found):
                    USER_DATA.classic_mode[self.act_name][self.lvl_name][NB_WORDS_KEY] = nb_words_found
            else:
                USER_DATA.classic_mode[self.act_name][self.lvl_name][NB_WORDS_KEY] = nb_words_found
            previous_xp_fraction: float = nb_words_previous_best / nb_words_300k
            # save quest word
            QUEST_WORD_KEY: str = "quest_word_done"
            award_quest_word_xp: bool = False
            if (QUEST_WORD_KEY in USER_DATA.classic_mode[self.act_name][self.lvl_name]):
                award_quest_word_xp = not(USER_DATA.classic_mode[self.act_name][self.lvl_name][QUEST_WORD_KEY]) and quest_word_done
                USER_DATA.classic_mode[self.act_name][self.lvl_name][QUEST_WORD_KEY] = USER_DATA.classic_mode[self.act_name][self.lvl_name][QUEST_WORD_KEY] or quest_word_done
            else:
                award_quest_word_xp = quest_word_done
                USER_DATA.classic_mode[self.act_name][self.lvl_name][QUEST_WORD_KEY] = quest_word_done

            # award newly acquired xp
            XP_KEY: str = "experience"
            USER_DATA.user_profile[XP_KEY] += int((xp_fraction - previous_xp_fraction) * XP_PER_LEVEL)
            if (award_quest_word_xp):
                USER_DATA.user_profile[XP_KEY] += XP_PER_LEVEL

            # save changes
            USER_DATA.save_changes()
            
        return


if __name__ == "__main__":
    # fill_gameplay_dict_with_solutions()
    # fill_daily_games_with_solutions()
    # print(is_valid("boy", "joy"))
    find_solutions("boy", "girl", ENGLISH_WORDS_DICTS["10k"])
