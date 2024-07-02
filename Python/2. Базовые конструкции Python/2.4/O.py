n, k = int(input()), int(input())
width = len(str(n * k))
for i in range(1, n + 1):
    for j in range(k):
        if not j % 2 and j != k - 1:
            print(str(i + 2 * n * (j // 2)).rjust(width, ' '), end=' ')
        elif not j % 2 and j == k - 1:
            print(str(i + 2 * n * (j // 2)).rjust(width, ' '))
        elif j % 2 and j != k - 1:
            print(str(2 * n * (j // 2 + 1) - (i - 1)).rjust(width, ' '), end=' ')
        else:
            print(str(2 * n * (j // 2 + 1) - (i - 1)).rjust(width, ' '))