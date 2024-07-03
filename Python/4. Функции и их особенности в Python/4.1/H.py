def is_palindrome(item):
    if isinstance(item, (int, str)):
        item = str(item)
        return item == item[::-1]
    elif isinstance(item, (tuple, list)):
        return item == item[::-1]
    else:
        return False
