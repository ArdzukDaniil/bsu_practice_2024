n = int(input())
m = int(input())
d = []
c = 0
for i in range(n):
    d.append(input())
for i in range(m):
    if input() in d:
        c += 1
if c > 0:
    print(c)
else:
    print("Таких нет")
