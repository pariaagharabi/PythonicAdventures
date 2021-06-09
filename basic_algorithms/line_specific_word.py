def find_word_line(file_name, target):
    with open(file_name, "r") as file_obj:
        lines = file_obj.readlines()
        result = []

        for i in range(len(lines)):
            count = lines[i].count(target)
            if count > 0:
                result.append((i+1, count))

        return result
