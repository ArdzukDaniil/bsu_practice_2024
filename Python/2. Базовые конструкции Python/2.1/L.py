a = input().strip()
b = input().strip()

max_len = max(len(a), len(b))
a = a.zfill(max_len)
b = b.zfill(max_len)

result = ""

for i in range(max_len):
    digit_a = int(a[i])
    digit_b = int(b[i])
    sum_digits = (digit_a + digit_b) % 10
    result += str(sum_digits)

print(result)
