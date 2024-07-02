words = input().split()

for i in range(1, len(words) + 1):
    print(' '.join(words[:i]))
