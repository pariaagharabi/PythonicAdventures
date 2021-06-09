def capital_letter(file_name):
    counter = 0

    with open(file_name, "r") as read_obj:
        words_list = read_obj.read().split()

        for word in words_list:
            if word.isupper():
                counter += 1

        return counter
