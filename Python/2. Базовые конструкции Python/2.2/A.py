print("Как Вас зовут?")
ss = input()

print(f"Здравствуйте, {ss}!")

print("Как дела?")
bb = input()

if bb.lower() == "хорошо":
    print("Я за вас рада!")
elif bb.lower() == "плохо":
    print("Всё наладится!")
