seen = {}
while True:
    line = input()
    if line == "":
        break
    for word in line.split():
        if word in seen:
            seen[word] += 1
        else:
            seen[word] = 1

for item, count in seen.items():
    print(f"{item} {count}")
