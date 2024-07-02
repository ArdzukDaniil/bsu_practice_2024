import itertools

M = int(input().strip())
menu = []
for _ in range(M):
    menu.append(input().strip())

N = int(input().strip())

cycle = itertools.cycle(menu)
schedule = list(itertools.islice(cycle, N))

for meal in schedule:
    print(meal)
