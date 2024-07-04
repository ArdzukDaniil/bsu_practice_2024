numbers = [int(x) for x in input().split()]
stats = []
for number in numbers:
    binary = bin(number)[2:]
    digits = len(binary)
    units = binary.count('1')
    zeros = digits - units
    stats.append({"digits": digits, "units": units, "zeros": zeros})
print(stats)
