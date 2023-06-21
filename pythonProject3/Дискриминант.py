def discr():
    a = input('a=')
    b = input('b=')
    c = input('c=')
    try:
        res=int(b)**2-4*int(a)*int(c)
    except ValueError:
        print('Неизвестные значения')
    else:
        print('D=',res)

discr()