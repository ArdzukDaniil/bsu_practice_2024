N = int(input().strip())

max_sum = -1
winner_name = ""

for _ in range(N):
    name = input().strip()
    number = input().strip()

    digit_sum = sum(int(digit) for digit in number)

    if digit_sum > max_sum:
        max_sum = digit_sum
        winner_name = name
    elif digit_sum == max_sum:
        winner_name = name

print(winner_name)
