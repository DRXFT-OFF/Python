def ex():           # creating a function to exclude incorrect input errors
    money = None
    while type(money) != int:       # we loop the input of values until money is int
        try:
            money = int(input('Invalid type. Enter an integer: '))
        except ValueError:
            continue
    return money
ans = input('Calculate the year/money: ').lower()       # we enter a value to understand what we want to find
if ans != 'year' and ans != 'money':            # we write lines to exclude incorrect input
    while ans != 'year' or ans != 'money':
        ans = input('Invalid value. Re-enter: ').lower()
        if ans == 'year' or ans == 'money':
            break
if ans == 'year':       # we write lines of code to calculate the year by the amount of money
    try:
        money = int(input('Enter money: '))     # enter the amount of money to calculate the number of years
    except ValueError:
        money = ex()        # exclusion of incorrect input errors
    years = 1       # creating a variable for counting years
    plus = 1        # creating a variable to add a value to the variable summ
    summ = 1        # creating a variable to stop the loop
    for i in range(money):      # creating a cycle to calculate the number of years
        years += 1
        plus += 1
        summ += plus
        if summ == money:       # stopping the loop
            break
        if summ > money:        # we exclude input errors that can lead to the endless operation of the program
            try:
                money = int(input('Invalid number. Enter other: '))
            except ValueError:
                money = ex()        # exclusion of incorrect input errors
            years = 1
            plus = 1        # we return the values of the variables to the original ones to calculate again
            summ = 1
    print(years, 'years')       # we output the number of years
if ans == 'money':          # we write lines of code to calculate the amount of money by year
    try:
        years = int(input('Enter years: '))
    except ValueError:          # we exclude input errors, do the same actions as in the ex function
        years = None
        while type(years) != int:       # we loop the input of values until years is int
            try:
                years = int(input('Invalid type. Enter an integer: '))
            except ValueError:
                continue
    plus = 1
    money = 0
    for i in range(years):      # creating a loop to calculate the amount of money
        money += plus       # each cycle we add 1 more than in the previous one
        plus += 1
    print(money, 'money')       # we output the value of money
