N = int(input().strip())

toy_counts = {}
child_toys = []

for _ in range(N):
    line = input().strip()
    name, toys = line.split(": ")
    toys_list = toys.split(", ")
    child_toys.append(toys_list)
    for toy in toys_list:
        if toy in toy_counts:
            toy_counts[toy].add(name)
        else:
            toy_counts[toy] = {name}

unique_toys = [toy for toy, children in toy_counts.items() if len(children) == 1]

unique_toys.sort()
for toy in unique_toys:
    print(toy)
