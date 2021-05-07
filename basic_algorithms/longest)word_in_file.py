#


def longes_word(file_name):
    with open(file_name, "r") as file_obj:
        words = file_obj.read().split()\

    max_len = len(max(words, key=len))

    for word in words:
        if len(word) == max_len:
            yield word
