s1 = int(input())
s2 = int(input())

while s2:
    s1, s2 = s2, s1 % s2
print(s1)
