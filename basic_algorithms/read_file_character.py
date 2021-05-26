def read_file_character_by_character(file_name):
    with open(file_name, "r") as file_obj:
        chars = file_obj.read()\
            .replace("\n", "")\
            .replace(" ", "")\
            .split()

    for char in chars:
        return char
