import sys
lines = sys.stdin.readlines()
query = lines[-1].strip().lower()
titles = [line.strip() for line in lines[:-1]]
found = False
for title in titles:
    if query in title.lower():
        print(title)
        found = True
if not found:
    print("Пока нет данных")
