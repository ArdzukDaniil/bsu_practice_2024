import sys

total_sum = 0
for line in sys.stdin:
    numbers = line.strip().split()
    for num in numbers:
        total_sum += int(num)

print(total_sum)
