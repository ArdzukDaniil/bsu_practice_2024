def snake(m, n, direction='H'):
    matrix = [[0 for _ in range(m)] for _ in range(n)]
    num = 1
    if direction == 'H':
        for i in range(n):
            if i % 2 == 0:
                for j in range(m):
                    matrix[i][j] = num
                    num += 1
            else:
                for j in range(m - 1, -1, -1):
                    matrix[i][j] = num
                    num += 1
    elif direction == 'V':
        for j in range(m):
            if j % 2 == 0:
                for i in range(n):
                    matrix[i][j] = num
                    num += 1
            else:
                for i in range(n - 1, -1, -1):
                    matrix[i][j] = num
                    num += 1
    for row in matrix:
        print(*row)
    return matrix
