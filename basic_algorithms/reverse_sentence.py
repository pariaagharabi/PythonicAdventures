# Reverse a sentence word by word.


def reverse_word_sentence(sentence):
    # conver a sentence to a list
    words = sentence.split(" ")

    reversed_words = words[::-1]
    reversed_sentence = " ".join(reversed_words)

    return reversed_sentence
