count = 0
str = input()
while (str != "Приехали!"):
    if "зайка" in str:
        count += 1
    str = input()
print(count)
