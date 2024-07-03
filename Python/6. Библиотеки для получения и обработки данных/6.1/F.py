def multiplication_matrix(n):
    matrix = []
    for i in range(1, n + 1):
        row = []
        for j in range(1, n + 1):
            row.append(i * j)
        matrix.append(row)
    for row in matrix:
        print(*row)
    return matrix
