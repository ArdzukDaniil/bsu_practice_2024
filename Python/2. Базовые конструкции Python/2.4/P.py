a, b = int(input()), int(input())
for i in range(1, a + 1):
    for j in range(1, a + 1):
        if j != a:
            print(f'{(str(i * j) + " " if b % 2 else str(i * j)).center(b)}|', end='')
        else:
            print(f'{(str(i * j) + " " if b % 2 else str(i * j)).center(b)}')
    if i * j != a * a:
        print(f'{"-"* ((b + 1) * a - 1)}')