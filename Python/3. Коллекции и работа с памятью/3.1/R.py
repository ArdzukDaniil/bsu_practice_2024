s = input()

current_char = s[0]
count = 1

for i in range(1, len(s)):
    if s[i] == current_char:
        count += 1
    else:
        print(f"{current_char} {count}")
        current_char = s[i]
        count = 1

print(f"{current_char} {count}")
