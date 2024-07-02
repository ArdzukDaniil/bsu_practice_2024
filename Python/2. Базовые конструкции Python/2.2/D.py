s1 = int(input())
s2 = int(input())
s3 = int(input())
if s1 > s2 and s1 > s3:
    print("1. Петя")
    if s2 > s3:
        print("2. Вася")
        print("3. Толя")
    else:
        print("2. Толя")
        print("3. Вася")
elif s2 > s1 and s2 > s3:
    print("1. Вася")
    if s1 > s3:
        print("2. Петя")
        print("3. Толя")
    else:
        print("2. Толя")
        print("3. Петя")
else:
    print("1. Толя")
    if s2 > s1:
        print("2. Вася")
        print("3. Петя")
    else:
        print("2. Петя")
        print("3. Вася")
