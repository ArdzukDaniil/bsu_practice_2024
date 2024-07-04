ingredients, dishes = [], set()
for _ in range(int(input())):
    ingredients.append(input())
for _ in range(int(input())):
    dishes.add(x := input())
    for i in range(int(input())):
        if input() not in ingredients:
            dishes.discard(x)
if dishes:
    for dish in sorted(dishes):
        print(dish)
else:
    print('Готовить нечего')