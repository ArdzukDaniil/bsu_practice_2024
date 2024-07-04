data = []
while (n := input()) != 'ФИНИШ':
    data.extend(n.lower().split())
max_count, data = 0, ''.join(data)
for symbol in set(data):
    max_count = max(max_count, data.count(symbol))
print(min([i for i in set(data) if data.count(i) == max_count]))