import math

x = float(input())
a = math.log(math.pow(x, 3 / 16), 32)
b = math.pow(x, math.cos((math.pi * x) / (2 * math.e)))
c = math.pow(math.sin(x / math.pi), 2)
print(a + b - c)