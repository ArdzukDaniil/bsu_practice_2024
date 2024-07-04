n = int(input())
porridges = ["Манная", "Гречневая", "Пшённая", "Овсяная", "Рисовая"]

for i in range(n):
    print(porridges[i % 5])
