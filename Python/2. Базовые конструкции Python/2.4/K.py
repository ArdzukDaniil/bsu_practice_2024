N = int(input().strip())
numbers = [int(input().strip()) for _ in range(N)]


def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    i = 3
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2
    return True


count_primes = 0
for num in numbers:
    if is_prime(num):
        count_primes += 1

print(count_primes)
