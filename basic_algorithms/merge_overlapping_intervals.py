def merge_overlapping_intervals(intervals):
    i = 0
    while i < len(intervals) - 1:
        found = False
        j = i + 1
        while j < len(intervals):
            result = merge(intervals[i], intervals[j])
            if result is not None:
                del intervals[j]
                del intervals[i]
                intervals.append(result)
                found = True
                break
            j += 1
        if not found:
            i += 1

    print(intervals)
    return intervals


def merge(first, second):
    if (second[0] <= first[0] <= second[1] or
        second[0] <= first[1] <= second[1] or
        first[0] <= second[0] <= first[1] or
            first[0] <= second[1] <= first[1]):
        return (min(first[0], second[0]), max(first[1], second[1]))

    return None
