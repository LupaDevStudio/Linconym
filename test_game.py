import numpy

import matplotlib.pyplot as plt

# Load the vector components
storage = numpy.load("export_wv.npz", allow_pickle=True)
wv = storage["data"]

# Load the words
file = open("wordlist_cleaned.txt", "r", encoding="utf-8")
lines = file.readlines()
words = [e.replace("\n", "") for e in lines]

# Define a search function


def dichotomy(word, dictionnary):
    a = 0
    b = len(dictionnary) - 1
    c = (a + b) // 2
    if word > dictionnary[b]:
        return None
    while dictionnary[c] != word and b - a > 1:
        if dictionnary[c] > word:
            b = c
        else:
            a = c
        c = (a + b) // 2
    if dictionnary[c] == word:
        return c
    return None


def norm(vec):
    return numpy.sqrt(numpy.sum(numpy.square(vec)))


def cosine_similarity(vec1, vec2):
    norm1 = norm(vec1)
    norm2 = norm(vec2)
    return numpy.dot(vec1, vec2) / (norm1 * norm2)


def project(vec1, vec2):
    return numpy.dot(vec1, vec2)


def get_vec(word):
    word_id = dichotomy(word, words)
    if word_id is None:
        return None
    return wv[word_id]


# print(get_vec("king"))

# print(cosine_similarity(get_vec("object"), get_vec("animal")))
base_word = "cat"
base_vec = get_vec("cat")

x_axis = get_vec("animal")
y_axis = get_vec("object")
center_x = project(base_vec, x_axis)
center_y = project(base_vec, y_axis)

guess_list = ["cat", "claw", "cute", "kitty",
              "pet", "feline", "paws", "carnivore"]
guess_vec_list = [get_vec(guess) for guess in guess_list]
# print(guess_vec_list)

x_coords = [project(guess_vec, x_axis) -
            center_x for guess_vec in guess_vec_list if guess_vec is not None]
y_coords = [project(guess_vec, y_axis) -
            center_y for guess_vec in guess_vec_list if guess_vec is not None]

plt.scatter(x_coords, y_coords)
plt.show()
