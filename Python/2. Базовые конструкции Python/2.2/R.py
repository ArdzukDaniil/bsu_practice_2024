a = float(input())
b = float(input())
c = float(input())

sides = sorted([a, b, c])
a, b, c = sides[0], sides[1], sides[2]

if c ** 2 == a ** 2 + b ** 2:
    print("100%")
elif c ** 2 > a ** 2 + b ** 2:
    print("велика")
else:
    print("крайне мала")
