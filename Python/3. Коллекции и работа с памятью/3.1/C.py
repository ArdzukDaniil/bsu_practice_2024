g = int(input())
for _ in range(int(input())):
    s = input()
    if g < len(s):
        print(f"{s[:g - 3]}...")
    elif g >= len(s):
        print(s)
