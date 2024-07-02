numbers = list(map(int, input().strip().split()))

gcd_result = numbers[0]

for num in numbers[1:]:
    while num != 0:
        gcd_result, num = num, gcd_result % num

print(gcd_result)
