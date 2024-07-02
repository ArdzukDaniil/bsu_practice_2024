N = int(input())
M = int(input())
K1 = int(input())
K2 = int(input())

N2 = (M * N - N * K1) / (K2 - K1)
N1 = N - N2
print(int(N1), int(N2))
