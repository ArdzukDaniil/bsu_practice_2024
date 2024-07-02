n = input()
ff = ""
ff2 = ""
s = []
s.append(int(n[0]))
s.append(int(n[1]))
s.append(int(n[2]))
m = max(s)
s.remove(m)
m2 = max(s)
s.remove(m2)
ff = ff + str(m) + str(m2)
if s[0] != 0:
    ff2 = str(s[0]) + str(m2)
else:
    ff2 = str(m2) + str(s[0])
print(ff2, ff)
