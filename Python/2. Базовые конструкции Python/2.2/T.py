s1 = input()
s2 = input()
s3 = input()
list = []
list.append(s1)
list.append(s2)
list.append(s3)
lst = []

for item in list:
    if "зайка" in item:
        lst.append(item)
if len(lst) < 2:
    print(lst[0], len(lst[0]))
elif len(lst) > 1:
    bb = lst[0]
    for i in lst:
        if bb > i:
            bb = i
    print(bb, len(bb))
