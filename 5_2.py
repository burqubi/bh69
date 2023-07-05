print('Здравствуйте, я простой калькулятор.')
a = int(input('Введите первое число: '))
sim = input('Выберите, что сделать: */:/+/-')
b = int(input('Введите второе число: '))

if sim == '*':
    print(a * b)
elif sim == ':':
    print(a / b)
elif sim == '+':
    print(a + b)
elif sim == '-':
    print(a - b)
else:
    print('Такого действия нет!!!!!!!!!')