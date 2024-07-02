import math

number = int(input().strip())

if number <= 1:
    print("NO")
else:
    is_prime = True
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        print("YES")
    else:
        print("NO")
