from sys import stdin
import json

data = [line.strip() for line in stdin]
print(data)
print({line.split(' == ')[0]: line.split(' == ')[1] for line in data[1:]})
D = {line.split(' == ')[0]: line.split(' == ')[1] for line in data[1:]}
with open(data[0], 'r', encoding="UTF-8") as f:
    records = json.load(f)
records.update(D)
if len(data) > 1:
    with open(data[0], 'w', encoding="UTF-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=4, sort_keys=True)