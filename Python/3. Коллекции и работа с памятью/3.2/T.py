n1 = input().split("; ")

n = sorted(map(int, set(n1)))
dd = []


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


for i, ob in enumerate(n):

    dd.clear()
    count = 0
    for j in n:
        if gcd(int(ob), int(j)) == 1:
            count += 1
            dd.append(j)
    if count > 0:
        print(f"{ob} - {', '.join(map(str, dd))}")
