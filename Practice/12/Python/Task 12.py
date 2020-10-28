
print('Программа расчёта факториала числа')
while True:
    try:
        a = int(input('Введите число:'))
        break
    except ValueError:
        print('Неверный ввод!!!')

if a < 0:
    print('Факториал может быть определён только на множестве целых неотрицательных чисел')
elif a == 0:
    print(1)
else:
    f = 1
    for i in range(1, a+1):
        f = f*i
    print(f)
