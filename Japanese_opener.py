from os import startfile, path, walk
from random import shuffle
def exec(number):
    while number > 14:
        try:
            number = int(input('Число слишком большое. Максимум 14 '))
        except ValueError:
            number = None
            while type(number) != int:
                try:
                    number = int(input('Неверное значение. Введите заново: '))
                except ValueError:
                    continue
    return number
ans = input('открыть файлы: выбор(1)/рандом(2) ').lower()
if 'os.system' in ans or 'os.popen' in ans or 'os.exec' in ans:
    quit('Доступ заблокирован')
while ans != 'выбор' and ans != 'рандом' and ans != '1' and ans != '2':
    ans = input('Ошибка. Введите снова: ')
    if 'os.system' in ans or 'os.popen' in ans or 'os.exec' in ans:
        quit('Доступ заблокирован')
if ans == 'выбор' or ans == '1':
    print('Темы:')
    for adress, dirs, files in walk("C://Users/home/Desktop/Японский"):
        for file in files:
            print(file[:-5])
    files_sp = input('Какие файлы хотите открыть? ').lower().split()
    if 'os.system' in files_sp or 'os.popen' in files_sp or 'os.exec' in files_sp:
        quit('Доступ заблокирован')
    test = False
    for adress, dirs, files in walk("C://Users/home/Desktop/Японский"):
        for file in files:
            for i in range(len(files_sp)):
                if files_sp[i] in file.lower():
                    startfile(path.join(adress, file))
                    test = True
        while test == False:
            files_sp.clear()
            files_sp = input('Не было найдено файлов с таким названием. Введите заново: ').lower().split()
            for file in files:
                for i in range(len(files_sp)):
                    if files_sp[i] in file.lower():
                        startfile(path.join(adress, file))
                        test = True
if ans == 'рандом' or ans == '2':
    try:
        number = int(input('Сколько файлов открыть?(макс 14) '))
        number = exec(number)
    except ValueError:
        number = None
        while type(number) != int:
            try:
                number = int(input('Неверное значение. Введите заново: '))
                number = exec(number)
            except ValueError:
                continue
    id_1 = list(range(0, 15))
    shuffle(id_1)
    num_files = id_1[:(number - 15)]
    for adress, dirs, files in walk("C://Users/home/Desktop/Японский"):
        for i in range(len(files)):
            if files.index(files[i]) in num_files:
                startfile(path.join(adress, files[files.index(files[i])]))
