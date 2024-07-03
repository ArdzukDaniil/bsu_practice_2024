n = int(input().strip())
factors = []
divisor = 2
while n > 1:
    while n % divisor == 0:
        factors.append(divisor)
        n //= divisor
    divisor += 1
result = ' * '.join(map(str, factors))
print(result)
