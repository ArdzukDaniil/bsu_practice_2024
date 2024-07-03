number = input()
result = ""

for digit in number:
    if int(digit) % 2 != 0:
        result += digit

print(result)
