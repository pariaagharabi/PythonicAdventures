def read_file_word(file_name):
    with open(file_name, "r") as file_obj:
        words = file_obj.read().split()

    return words
