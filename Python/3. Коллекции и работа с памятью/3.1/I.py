result = []
while True:
    line = input()
    if line == "":
        break
    stripped_line = line.split('#')[0].rstrip()
    if stripped_line:
        result.append(stripped_line)
for line in result:
    print(line)
