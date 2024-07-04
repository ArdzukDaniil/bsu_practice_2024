from sys import stdin

files = [name.strip() for name in stdin]
data = []
with open(files[0]) as f:
    for line in f:
        data.append(line.split())
D = dict(zip([1, 2, 3], ['>', '<', '==']))
for n in range(1, len(files)):
    with open(files[n], 'w') as f:
        for line in data:
            for i in line:
                if eval('len(list(filter(lambda x: not int(x) % 2, i)))'
                        + D[n] +
                        'len(list(filter(lambda x: int(x) % 2, i)))'):
                    print(i, end=' ', file=f)
            print('\n', end='', file=f)