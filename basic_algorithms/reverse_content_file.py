def reverse_content_file(file_name, new_file):
    with open(file_name, "r") as read_obj:
        lines = read_obj.read()

    with open(new_file, "w") as write_obj:
        reverse_lines = lines[::-1]
        write_obj.write(reverse_lines)
