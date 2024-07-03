def to_string(*data, sep=' ', end='\n'):
    result = ''
    for i, item in enumerate(data):
        result += str(item)
        if i < len(data) - 1:
            result += sep
    result += end
    return result
