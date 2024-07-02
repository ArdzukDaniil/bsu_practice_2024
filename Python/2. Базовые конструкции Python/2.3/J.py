x, y = 0, 0

while True:
    direction = input().strip()
    if direction == "СТОП":
        break
    steps = int(input().strip())

    if direction == "СЕВЕР":
        y += steps
    elif direction == "ЮГ":
        y -= steps
    elif direction == "ВОСТОК":
        x += steps
    elif direction == "ЗАПАД":
        x -= steps

print(f"{y}\n{x}")
