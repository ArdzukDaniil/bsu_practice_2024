d = int(input().strip())

results = []
for a in range(1, d - 1):
    for b in range(1, d - a):
        c = d - a - b
        if c >= 1:
            results.append((a, b, c))

print("А Б В")
for result in results:
    print(result[0], result[1], result[2])
