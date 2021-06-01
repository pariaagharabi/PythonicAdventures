def detect_duplicate_dictionary(items, key=None):
    result = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in result:
            yield item
            result.add(val)
