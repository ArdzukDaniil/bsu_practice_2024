number = list(map(int, (input() + input())))
print(str(max(number)) + str((sum(number) - max(number) - min(number)) % 10) + str(min(number)))