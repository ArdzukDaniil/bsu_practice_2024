s1 = input()
s2 = ""
d1 = int(s1[1]) + int(s1[2])
d2 = int(s1[0]) + int(s1[1])
if d1 > d2:
    s2 = s2 + str(d1) + str(d2)
else:
    s2 = s2 + str(d2) + str(d1)
print(s2)
