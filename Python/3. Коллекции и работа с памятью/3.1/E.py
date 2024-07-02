s = input()
s.lower().split()
if s == s[::-1]:
    print("YES")
else:
    print("NO")
