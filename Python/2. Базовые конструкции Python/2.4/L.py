n, k = int(input()), int(input())
width = len(str(n * k))
for i in range(1, n + 1):
    for j in range(k * (i - 1) + 1, k * i + 1):
        if j == k * i:
            print(str(j).rjust(width, ' '))
        else:
            print(str(j).rjust(width, ' '), end=' ')