size = int(input().strip())

for i in range(1, size + 1):
    row = []
    for j in range(1, size + 1):
        row.append(str(i * j))
    print(" ".join(row))
