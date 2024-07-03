def make_matrix(size, value=0):
    if isinstance(size, int):
        size = (size, size)
    return [[value] * size[0] for _ in range(size[1])]
