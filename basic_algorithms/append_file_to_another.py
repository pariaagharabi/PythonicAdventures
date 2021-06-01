def append_files(first_file, second_file):
    with open(first_file, "r") as read_obj:
        infile = read_obj.read()

    with open(second_file, "a") as append_obj:
        append_obj.write(infile)
