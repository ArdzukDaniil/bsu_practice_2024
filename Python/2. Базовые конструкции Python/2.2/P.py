speed_petya = int(input())
speed_vasya = int(input())
speed_tolia = int(input())

competitors = [("Петя", speed_petya), ("Вася", speed_vasya), ("Толя", speed_tolia)]
competitors.sort(key=lambda x: x[1], reverse=True)

first = competitors[0][0]
second = competitors[1][0]
third = competitors[2][0]

print(f'{"": ^8}{first: ^8}{"": ^8}')
print(f'{second: ^8}{"": ^8}{"": ^8}')
print(f'{"": ^8}{"": ^8}{third: ^8}')
print(f'{"II": ^8}{"I": ^8}{"III": ^8}')
