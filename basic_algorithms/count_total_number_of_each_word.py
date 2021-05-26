def count_total_number_of_each_word(file_name):
    counter = dict()

    with open(file_name, "r") as file_obj:
        words = file_obj.read().split()

        for word in words:
            if word in counter:
                counter[word] += 1
            else:
                counter[word] = 1
    return counter
