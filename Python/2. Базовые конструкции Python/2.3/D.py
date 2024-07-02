s1 = int(input())
s2 = int(input())
len = abs(s2 - s1) + 1
if (s1 > s2):
    for i in range(len):
        print(s1, end=' ')
        s1 = s1 - 1
elif (s1 < s2):
    for i in range(s1, s2 + 1):
        print(i, end=' ')
elif (s1 == s2):
    print(s1)
