n = int(input().strip())
current_number = 1
row_length = 1

while current_number <= n:
    for _ in range(row_length):
        if current_number > n:
            break
        print(current_number, end=' ')
        current_number += 1
    print()
    row_length += 1
