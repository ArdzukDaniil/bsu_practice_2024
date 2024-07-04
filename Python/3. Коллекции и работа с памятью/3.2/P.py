seen_near_zaika = set()
while True:
    line = input()
    if line == "":
        break
    words = line.split()
    for i, word in enumerate(words):
        if word == "зайка":
            if i > 0:
                seen_near_zaika.add(words[i - 1])
            if i < len(words) - 1:
                seen_near_zaika.add(words[i + 1])

for item in seen_near_zaika:
    print(item)
