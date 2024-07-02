n = int(input())
m = int(input())
d = dict()
for i in range(n + m):
    word = input()
    if word not in d:
        d[word] = 1
    else:
        d[word] += 1
count = 0
for key in d:
    if d[key] == 1:
        count += 1
if count > 0:
    print(count)
else:
    print("Таких нет")
