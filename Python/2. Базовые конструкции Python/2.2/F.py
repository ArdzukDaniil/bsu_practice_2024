s1 = int(input())
if (s1 % 4 == 0 and s1 % 100 != 0) or (s1 % 400 == 0):
    print("YES")
else:
    print("NO")
