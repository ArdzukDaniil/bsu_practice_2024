N = int(input().strip())
count = 0

for _ in range(N):
    has_zayka = False
    while True:
        word = input().strip()
        if word == "ВСЁ":
            break
        if word == "зайка":
            has_zayka = True
    if has_zayka:
        count += 1

print(count)
