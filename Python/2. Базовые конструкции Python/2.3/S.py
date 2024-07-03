low = 1
high = 1000
tries = 0

while True:
    guess = (low + high) // 2
    print(guess)
    response = input().strip()
    tries += 1

    if response == "Угадал!":
        break
    elif response == "Больше":
        low = guess + 1
    elif response == "Меньше":
        high = guess - 1

    if tries >= 10:
        break
