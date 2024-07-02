d = set(input())
s = set(input())
u = s & d
for i in u:
    print(i, end="")
