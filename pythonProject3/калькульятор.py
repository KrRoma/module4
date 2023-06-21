import math
def calculate():
    print('Укажите интересующую вас опеацию')
    print('+ - cложение')
    print('- - вычитание')
    print('* - умножение')
    print('/ - деление')
    print('D - вычесление дискриминанта')
    print('R - вычесление корня числа')

    operation=input()
    operation=operation.upper()

    if operation=='+':
        num1=input('Введите 1 число: ')
        num2=input('Введите 2 число: ')
        try:
            res=int(num1)+int(num2)
        except ValueError:
            print('Неизвестные значеия')
        else:
            print('Сумма чисел =',res)
    elif operation=='-':
        num1=input('Введите 1 число: ')
        num2=input('Введите 2 число: ')
        try:
            res=int(num1)-int(num2)
        except ValueError:
            print('Неизвестные значеия')
        else:
            print('Разность чисел =',res)
    elif operation=='*':
        num1=input('Введите 1 число: ')
        num2=input('Введите 2 число: ')
        try:
            res=int(num1)*int(num2)
        except ValueError:
            print('Неизвестные значеия')
        else:
            print('Произведение чисел =',res)
    elif operation=='/':
        num1=input('Введите 1 число: ')
        num2=input('Введите 2 число: ')
        try:
            res=int(num1)/int(num2)
        except ValueError:
            print('Неизвестные значеия')
        else:
            print('Частное чисел =',res)
    elif operation=='D':
        a = input('a=')
        b = input('b=')
        c = input('c=')
        try:
            res = int(b) ** 2 - 4 * int(a) * int(c)
        except ValueError:
            print('Неизвестные значения')
        else:
            print('D=', res)
    elif operation=='R':
        num1 = input('Введите число: ')
        try:
            res =math.sqrt(int(num1))
        except ValueError:
            print('Неизвестные значеия')
        else:
            print('Квадратный корень числа=', res)
    else:
        print('Неизвестная операция. Повторите ввод')

    calculate()

calculate()