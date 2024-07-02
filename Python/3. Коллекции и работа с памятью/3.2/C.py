s = set()
for i in range(int(input())):
    b = set(input().split(" "))
    s = s | b
for i in s:
    print(i)
