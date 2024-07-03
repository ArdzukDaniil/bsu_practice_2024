def sum_of_digits_in_base(number, base):
    sum_digits = 0
    while number > 0:
        sum_digits += number % base
        number //= base
    return sum_digits


number = int(input().strip())

max_sum_digits = -1
best_base = -1

for base in range(2, 11):
    sum_digits = sum_of_digits_in_base(number, base)
    if sum_digits > max_sum_digits:
        max_sum_digits = sum_digits
        best_base = base
    elif sum_digits == max_sum_digits:
        if base < best_base:
            best_base = base

print(best_base)
