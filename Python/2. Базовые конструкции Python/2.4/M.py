n, k = int(input()), int(input())
width = len(str(n * k))
for i in range(1, n + 1):
    for j in range(i, i + n * (k - 1) + 1, n):
        if j == i + n * (k - 1):
            print(str(j).rjust(width, ' '))
        else:
            print(str(j).rjust(width, ' '), end=' ')