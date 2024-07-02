N = int(input().strip())
players = []
for _ in range(N):
    players.append(input().strip())

for i in range(N):
    for j in range(i + 1, N):
        print(f"{players[i]} - {players[j]}")
