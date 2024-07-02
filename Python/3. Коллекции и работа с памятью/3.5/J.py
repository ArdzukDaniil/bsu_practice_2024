file_in, number = input(), int(input())
data = []
with open(file_in) as f:
    for line in f:
        data.append(line)
for line in data[-number:]:
    print(line.strip())