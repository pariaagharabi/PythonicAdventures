def remove_duplicate_lines(input_file, output_file):
    with open(input_file, "r") as read_obj:
        lines = read_obj.readlines()

    with open(output_file, "w") as write_obj:
        result = set()

        for line in lines:
            if line not in result:
                write_obj.write(line)
                result.add(line)
