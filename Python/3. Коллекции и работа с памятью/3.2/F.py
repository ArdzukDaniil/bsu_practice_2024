n = int(input())
m = int(input())

manna_lovers = set()
oatmeal_lovers = set()

for _ in range(n + m):
    name = input()
    if name not in manna_lovers:
        manna_lovers.add(name)
    else:
        oatmeal_lovers.add(name)

single_lovers = sorted(manna_lovers ^ oatmeal_lovers)

if single_lovers:
    for name in single_lovers:
        print(name)
else:
    print("Таких нет")
