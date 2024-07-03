def make_linear(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(make_linear(item))
        else:
            result.append(item)
    return result
