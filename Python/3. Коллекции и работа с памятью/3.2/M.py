menu, new_menu = set(), set()
for _ in range(int(input())):
    menu.add(input())
for _ in range(int(input())):
    for j in range(int(input())):
        new_menu.add(input())
diff = sorted(menu - new_menu)
if diff:
    for dish in diff:
        print(dish)
else:
    print('Готовить нечего')