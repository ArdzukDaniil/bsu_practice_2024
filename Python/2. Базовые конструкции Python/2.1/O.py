hour = int(input())
min = int(input())
T = int(input())
ch = T // 60
ost = T % 60
hour += ch
min += ost

if min >= 60:
    hour += min // 60
    min = min % 60

if hour >= 24:
    hour = hour % 24

ss = f"{hour:02}"
ss1 = f"{min:02}"

print(f"{ss}:{ss1}")
