s1 = int(input())
s2 = int(input())
ss = 0
bb = abs(s1 * s2)
while s2:
    s1, s2 = s2, s1 % s2

print(bb // s1)
