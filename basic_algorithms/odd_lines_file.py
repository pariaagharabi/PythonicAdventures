def get_odd_lines_file(file_name, new_file):
    with open(file_name, "r") as read_obj:
        lines = read_obj.readlines()

    with open(new_file, "w") as write_obj:
        for i in range(len(lines)):
            if (i+1) % 2 == 0:
                write_obj.write(lines[i])
