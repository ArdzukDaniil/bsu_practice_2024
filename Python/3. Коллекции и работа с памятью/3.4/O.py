from itertools import permutations

items = []
for _ in range(int(input())):
    items.extend([item for item in input().split(', ')])
for item in sorted(permutations(items, 3)):
    print(' '.join(item))