s1 = float(input())
sum = 0
while (s1 != 0):
    if s1 >= 500:
        sum = sum + s1 * 0.9
    else:
        sum = sum + s1
    s1 = float(input())
print(float(sum))
