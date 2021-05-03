# get two elements whose sum is equal to a certain number n


def get_pairs_v1(lst, num):
    for i in lst:
        for j in lst:
            if (i + j == num):
                return i, j


def get_pairs_v2(lst, num):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if (lst[i] + lst[j] == num):
                return lst[i], lst[j]
