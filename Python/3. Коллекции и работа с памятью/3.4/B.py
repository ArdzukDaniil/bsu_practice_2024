group1 = input().strip().split(', ')
group2 = input().strip().split(', ')

pairs = list(zip(group1, group2))

for pair in pairs:
    print(f"{pair[0]} - {pair[1]}")
