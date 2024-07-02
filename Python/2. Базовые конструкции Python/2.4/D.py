n = int(input().strip())
total_sum = 0

for _ in range(n):
    number = input().strip()
    total_sum += sum(int(digit) for digit in number)

print(total_sum)
