import numpy

import matplotlib.pyplot as plt


# Load the words
file = open("wordlist_cleaned.txt", "r", encoding="utf-8")
lines = file.readlines()
words = [e.replace("\n", "") for e in lines]


def normalise_by_column(matrix):
    return numpy.repeat(
        1 / numpy.expand_dims(numpy.sqrt(numpy.sum(numpy.square(matrix), axis=1)), axis=1), matrix.shape[1], axis=1) * matrix


def create_subspace_matrix(matrix, axis_list):
    new_matrix = numpy.zeros(
        (matrix.shape[0], len(axis_list)), dtype=numpy.float32)
    for i in range(matrix.shape[0]):
        for j in range(len(axis_list)):
            new_matrix[i, j] = project(matrix[i], axis_list[j])
    return normalise_by_column(new_matrix)


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


def word_similarity(word1, word2):
    vec1 = get_vec(word1)
    vec2 = get_vec(word2)
    return cosine_similarity(vec1, vec2)


def project(vec1, vec2):
    return numpy.dot(vec1, vec2)


def get_vec(word):
    word_id = dichotomy(word, words)
    if word_id is None:
        print(word)
        return None
    return wv[word_id]


def find_most_similar_word(vec):
    # do it with excluded words
    max_similarity = 0
    max_id = 0
    for i in range(wv.shape[0]):
        similarity = cosine_similarity(vec, wv[i])
        if similarity > max_similarity:
            max_similarity = similarity
            max_id = i
    return words[max_id]


def get_randow_vec():
    res = numpy.cos(numpy.random.random(wv.shape[1]) * 2 * numpy.pi)
    return res / norm(res)


# Load the vector components
storage = numpy.load("export_wv.npz", allow_pickle=True)
data = storage["data"]


# data_n = numpy.repeat(
#     1 / numpy.expand_dims(numpy.sqrt(numpy.sum(numpy.square(data), axis=1)), axis=1), 300, axis=1) * data

wv = data

# word_axis_list = ["hard", "red", "concept", "chair", "crocodile",
#                   "philosophy", "iron", "administration", "behavior", "leader", "female", "sad", "genius", "war"]
# vec_axis_list = [get_vec(word) for word in word_axis_list]
vec_axis_list = [get_randow_vec() for i in range(30)]

data_p = create_subspace_matrix(data, vec_axis_list)
wv = data_p


start_word = "state"
end_word = "cat"


attempt_word = start_word
similarity = word_similarity(end_word, attempt_word)
end_vec = get_vec(end_word)

while True:
    print("Enter your combination : ", end="")
    word_list = []
    combination = input()
    symbol_list = []
    last_idx = 0
    for idx, car in enumerate(combination):
        if car == "+" or car == "-":
            word_list.append(combination[last_idx:idx])
            symbol_list.append(car)
            last_idx = idx + 1
        if idx == len(combination) - 1:
            word_list.append(combination[last_idx:idx + 1])
    # print(word_list)
    for word in word_list[1:]:
        if word == start_word:
            print("Unauthorized input")
            exit()
    value_list = []
    for word in word_list:
        value_list.append(get_vec(word))
    # print(len(value_list))
    # print(value_list[0][:3])
    combined_vec = value_list[0].copy()
    for i, symbol in enumerate(symbol_list):
        if symbol == "+":
            combined_vec += value_list[i + 1]
        elif symbol == "-":
            combined_vec -= value_list[i + 1]
    # print(combined_vec[:3])
    combined_vec = combined_vec / norm(combined_vec)
    print("most similar : ", find_most_similar_word(combined_vec))

while similarity < 0.9:
    print("Enter your combination : ", end="")
    print(start_word, end="")
    combination = start_word + input()
    word_list = []
    symbol_list = []
    last_idx = 0
    for idx, car in enumerate(combination):
        if car == "+" or car == "-":
            word_list.append(combination[last_idx:idx])
            symbol_list.append(car)
            last_idx = idx + 1
        if idx == len(combination) - 1:
            word_list.append(combination[last_idx:idx + 1])
    # print(word_list)
    for word in word_list[1:]:
        if word == start_word:
            print("Unauthorized input")
            exit()
    value_list = []
    for word in word_list:
        value_list.append(get_vec(word))
    # print(len(value_list))
    # print(value_list[0][:3])
    combined_vec = value_list[0].copy()
    for i, symbol in enumerate(symbol_list):
        if symbol == "+":
            combined_vec += value_list[i + 1]
        elif symbol == "-":
            combined_vec -= value_list[i + 1]
    # print(combined_vec[:3])
    combined_vec = combined_vec / norm(combined_vec)
    similarity = cosine_similarity(end_vec, combined_vec)
    print(similarity)
    print("most similar : ", find_most_similar_word(combined_vec))

print("You win")
