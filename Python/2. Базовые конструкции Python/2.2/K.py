d = input()
list = []
for i in d:
    list.append(int(i))
sum = max(list) + min(list)
list.remove(max(list))
list.remove(min(list))

if list[0] * 2 == sum:
    print("YES")
else:
    print("NO")
