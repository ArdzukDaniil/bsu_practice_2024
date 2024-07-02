g = input()
s = g.replace(" ", "")
g = s.lower()
ss = list(g)
s1 = list(g)
s1.reverse()
if s1 == ss:
    print("YES")
else:
    print("NO")
