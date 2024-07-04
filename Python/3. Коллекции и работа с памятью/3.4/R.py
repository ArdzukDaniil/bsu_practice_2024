expression = input()

print("a b c f")
for a in [0, 1]:
    for b in [0, 1]:
        for c in [0, 1]:
            result = eval(expression)
            print(f"{a} {b} {c} {result}")
