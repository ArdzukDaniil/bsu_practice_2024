counter = 0
for _ in range(int(input())):
    if (n := input()) == n[::-1]:
        counter += 1
print(counter)