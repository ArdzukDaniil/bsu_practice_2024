g = int(input())
for i in range(g):
    s = input()
    if "зайка" in s:
        print(s.find("зайка") + 1)
    else:
        print("Заек нет =(")
