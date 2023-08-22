from os import startfile, path, walk
from random import shuffle
def exec(number, len_files):
    while number > len_files - 1:
        try:
            number = int(input(f'Число слишком большое. Максимум {len_files - 1} '))
        except ValueError:
            number = None
            while type(number) != int:
                try:
                    number = int(input('Неверное значение. Введите заново: '))
                except ValueError:
                    continue
    return number
len_files = 0
try:
    filepath = input("Введите путь до папки: ")
    for adress, dirs, files in walk(filepath):
        len_files = len(files)
    number = int(input(f'Сколько файлов открыть?(макс {len_files - 1}) '))
    number = exec(number, len_files)
except ValueError:
    number = None
    while type(number) != int:
        try:
            number = int(input('Неверное значение. Введите заново: '))
            number = exec(number, len_files)
        except ValueError:
            continue
id_1 = list(range(0, len_files))
shuffle(id_1)
num_files = id_1[:(number - len_files)]
for adress, dirs, files in walk(filepath):
    for i in range(len(files)):
        if files.index(files[i]) in num_files:
            startfile(path.join(adress, files[files.index(files[i])]))
