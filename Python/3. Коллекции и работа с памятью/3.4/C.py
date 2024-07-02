start, end, step = map(float, input().split())

current = start
while current <= end:
    print(f"{current:.2f}")
    current += step
