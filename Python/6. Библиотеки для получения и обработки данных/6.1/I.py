def rotate(matrix, angle):
    n = len(matrix)
    m = len(matrix[0])
    result = [[0 for _ in range(n)] for _ in range(m)]
    if angle == 90:
        for i in range(n):
            for j in range(m):
                result[j][n - i - 1] = matrix[i][j]
    elif angle == 180:
        for i in range(n):
            for j in range(m):
                result[n - i - 1][m - j - 1] = matrix[i][j]
    elif angle == 270:
        for i in range(n):
            for j in range(m):
                result[m - j - 1][i] = matrix[i][j]
    elif angle == 360:
        for i in range(n):
            for j in range(m):
                result[i][j] = matrix[i][j]
    for row in result:
        print(*row)
    return result
