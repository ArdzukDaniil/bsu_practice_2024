from itertools import permutations

n = int(input())
names = [input() for _ in range(n)]

for permutation in sorted(permutations(names)):
    print(", ".join(permutation))
