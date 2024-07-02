g = int(input())
flag = True
for i in range(g):
    if (w := input())[0] not in "абв":
        print("NO")
        flag = False
        break
if flag:
    print("YES")
