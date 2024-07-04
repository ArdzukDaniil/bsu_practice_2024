n = int(input())

children = {}
for _ in range(n):
    name, *likes = input().split()
    children[name] = set(likes)

target_dish = input()

lovers = []
for name, dishes in children.items():
    if target_dish in dishes:
        lovers.append(name)

if lovers:
    for name in sorted(lovers):
        print(name)
else:
    print("Таких нет")
