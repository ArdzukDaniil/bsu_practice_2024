g, lengths = '', [0]
for j in range(1, (x := int(input())) + 1):
    g += str(j) + ' '
    if j in (sum(range(i)) for i in range(j + 2)):
        lengths.append(len(g) - 1)
        g = ''
lengths.append(len(g) - 1)
d = 1
for z in range(1, x + 1):
    if z - 1 in (sum(range(i)) for i in range(z + 2)):
        print(f"{' ' * ((max(lengths) - lengths[d]) // 2)}{z}", end=' ' if z != 1 else '\n')
        d += 1
    else:
        print(z, end='\n' if z in (sum(range(i)) for i in range(z + 2)) else ' ')