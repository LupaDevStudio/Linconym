# Rules

## How the game plays

The user has at the beginning of the game two words, the first one labelled as the *start word* and the other one as the *end word*.

The goal of the game is to create a path of words between the *start word* and the *end word*. To do this, three types of moves are possible:

1. **Change a single letter**: the user creates a new word using the letters of the previous one, he is allowed to change the order of all letters and additionally to change a single one of them. If a letter appears twice in the word, he can only change one of its occurrences. For example : `mouse --> moose`
2. **Remove one letter**: the user creates a new word by changing the order of the letters of the previous word and removing one of them. If a letter appears twice in the word, he can only remove one of its occurrences. For example : `muse --> sum`
3. **Add one letter**: the user creates a new word by changing the order of the letters of the previous word and adding a new letter. For example : `sum --> must`

Each one of the successive words has to be in the dictionary.

Here a complete example:

```
start word : boy
end word : girl

boy -> bio # change
bio -> big # change
big -> pig # change
pig -> grip # add
grip -> girl # add
```

Once the path is finished its length is computed including the start and end words to compute the number of stars obtained.