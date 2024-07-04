with open("numbers.num", "rb") as f:
    data = f.read()
print(sum([int.from_bytes(data[i:i + 2], "big") for i in range(0, len(data), 2)]) % 2 ** 16)
