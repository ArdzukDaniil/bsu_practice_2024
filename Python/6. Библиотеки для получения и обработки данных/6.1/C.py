from math import comb

n, m = map(int, input().split())
print(comb(n, m) * m // n, comb(n, m))