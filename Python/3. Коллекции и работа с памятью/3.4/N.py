from itertools import permutations

items = []
for _ in range(int(input())):
    items.append(input())
for i in sorted(permutations(items, 3)):
    print(', '.join(i))