def bubble_sort(lst):
    for _ in range(0, len(lst)):
        for j in range(0, len(j) - 1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
