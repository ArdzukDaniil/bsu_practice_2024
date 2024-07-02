import sys

total_change = 0
count = 0

for line in sys.stdin:
    parts = line.split()
    name = parts[0]
    height_last_month = int(parts[1])
    height_now = int(parts[2])

    total_change += (height_now - height_last_month)
    count += 1

average_change = total_change / count
print(round(average_change))
