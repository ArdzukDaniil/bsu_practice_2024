prod = input()
cost = int(input())
weight = int(input())
count = int(input())

total = cost * weight
change = count - total

width = 35
print("================Чек================")
print(f"Товар: {prod:>{width - 7}}")
print(f"Цена:{f'{weight}кг * {cost}руб/кг'.rjust(width - 5)}")
print(f"Итого: {f'{total}руб'.rjust(width - 7)}")
print(f"Внесено: {f'{count}руб'.rjust(width - 9)}")
print(f"Сдача: {f'{change}руб'.rjust(width - 7)}")
print("===================================")
