import math

N = int(input().strip())
numbers = []
for _ in range(N):
    numbers.append(int(input().strip()))

gcd_result = numbers[0]
for num in numbers[1:]:
    while num != 0:
        gcd_result, num = num, gcd_result % num

print(gcd_result)
