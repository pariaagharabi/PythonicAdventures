# count the frequency of words repeated in a text file?


def get_file_words_repetition(file_name):
    word_counter = dict()

    with open(file_name, "r") as file_object:
        words_list = file_object.read()\
            .lower()\
            .replace("\n", " ")\
            .replace(". ", " ")\
            .split(" ")

        for word in words_list:
            if word in word_counter:
                word_counter[word] += 1
            else:
                word_counter[word] = 1

        return word_counter
