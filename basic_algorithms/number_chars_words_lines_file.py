def number_chars_worlds_lines(file_name):
    number_of_lines = 0
    number_of_words = 0
    number_of_characters = 0

    with open(file_name, "r") as file_obj:
        for line in file_obj:
            words = line.split()
            number_of_lines += 1
            number_of_words += len(words)
            number_of_characters += len(line)

    return (f"Lines:\n\t{number_of_lines}\nWords:\n\t{number_of_words}\nCharacters:\n\t{number_of_characters}")
