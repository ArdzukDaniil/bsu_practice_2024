from itertools import product

n, m = int(input()), int(input())
for i in range(n):
    line = product(range(1, m + 1), [i * m])
    print(' '.join(map(lambda x: str(sum(x)).rjust(len(str((n - 1 - i) * m + sum(x))), ' '), line)))