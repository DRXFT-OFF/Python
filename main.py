def ex():
    money = None
    while type(money) != int:
        try:
            money = int(input('Invalid type. Enter an integer: '))
        except ValueError:
            continue
    return money
ans = input('Calculate the year/money: ').lower()
if ans != 'year' and ans != 'money':
    while ans != 'year' or ans != 'money':
        ans = input('Invalid value. Re-enter: ').lower()
        if ans == 'year' or ans == 'money':
            break
if ans == 'year':
    try:
        money = int(input('Enter money: '))
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
                money = int(input('Invalid number. Enter other: '))
            except ValueError:
                money = ex()
            years = 1
            plus = 1
            summ = 1
    print(years, 'years')
if ans == 'money':
    try:
        years = int(input('Enter years: '))
    except ValueError:
        years = None
        while type(years) != int:
            try:
                years = int(input('Invalid type. Enter an integer: '))
            except ValueError:
                continue
    plus = 1
    money = 0
    for i in range(years):
        money += plus
        plus += 1
    print(money, 'money')
