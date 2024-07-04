n = int(input())
titles = [input().strip() for _ in range(n)]
query = input().strip().lower()

results = [title for title in titles if query in title.lower()]

for result in results:
    print(result)
