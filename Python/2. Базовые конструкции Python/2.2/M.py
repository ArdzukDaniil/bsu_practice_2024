s1 = int(input())
s2 = int(input())
s3 = int(input())

if s1 // 10 == s2 // 10 and s1 // 10 == s3 // 10:
    print(s1 // 10)
elif s1 % 10 == s2 % 10 and s1 % 10 == s3 % 10:
    print(s1 % 10)
