def stairs(vector):
    n = len(vector)
    matrix = []
    for i in range(n):
        row = vector[i:] + vector[:i]
        matrix.append(row)
    return matrix
