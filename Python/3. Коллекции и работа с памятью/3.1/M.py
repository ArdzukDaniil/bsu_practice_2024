n = int(input())
numbers = [int(input()) for _ in range(n)]
p = int(input())

for number in numbers:
    print(number ** p)
