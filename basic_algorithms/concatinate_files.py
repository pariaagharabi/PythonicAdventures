def concatinate_files(first_file, second_file, concat_file):
    files_name = [first_file, second_file]

    with open(concat_file, "w") as out_file:
        for file_name in files_name:
            with open(file_name) as in_file:
                for line in in_file:
                    out_file.write(line)
