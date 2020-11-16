a = input('Введите первое число:')
b = input('Введите второе число:')
num1 = int(a)
num2 = int(b)

if num2 == 0:
    chastnoe = 'Бесконечность'
    print('Частное от 2 чисел равно:', str(chastnoe))
else:
    chastnoe = num1 / num2
    print('Частное от 2 чисел равно:', str(chastnoe))
