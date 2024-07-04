file1 = input("Введите имя первого файла: ")
file2 = input("Введите имя второго файла: ")
output_file = input("Введите имя выходного файла: ")

with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
    words1 = set(f1.read().split())
    words2 = set(f2.read().split())

unique_words = sorted((words1 ^ words2))

with open(output_file, 'w', encoding='utf-8') as f_out:
    f_out.write('\n'.join(unique_words))
