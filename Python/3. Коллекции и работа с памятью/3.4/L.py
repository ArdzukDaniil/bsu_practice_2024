items = []
for _ in range(int(input())):
    items.extend([item for item in input().split(', ')])
for i, item in enumerate(sorted(items), start=1):
    print(f'{i}. {item}')