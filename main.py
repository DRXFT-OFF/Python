def ex():
    money = None
    while type(money) != int:
        try:
            money = int(input('Некорректный тип. Введите целое число: '))
        except ValueError:
            continue
    return money
ans = input('Вычислить год/деньги ').lower()
if ans != 'год' and ans != 'деньги':
    while ans != 'год' or ans != 'деньги':
        ans = input('Неверное значение. Введите заново: ').lower()
        if ans == 'год' or ans == 'деньги':
            break
if ans == 'год':
    try:
        money = int(input('Деньги: '))
    except ValueError:
        money = ex()
    years = 1
    plus = 1
    summ = 1
    for i in range(money):
        years += 1
        plus += 1
        summ += plus
        if summ == money:
            break
        if summ > money:
            try:
                money = int(input('Неверное число. Введите другое: '))
            except ValueError:
                money = ex()
            years = 1
            plus = 1
            summ = 1
    print(years, 'лет')
if ans == 'деньги':
    try:
        years = int(input('Года: '))
    except ValueError:
        years = None
        while type(years) != int:
            try:
                years = int(input('Некорректный тип. Введите целое число: '))
            except ValueError:
                continue
    plus = 1
    money = 0
    for i in range(years):
        money += plus
        plus += 1
    print(money, 'денег')
