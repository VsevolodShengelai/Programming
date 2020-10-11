# Тест на простоту числа
# Теорема Вильсона
# p — простое число тогда и только тогда, когда (p − 1)! + 1 делится на p
import math

print('Программа рассчёта факториала числа')
while True:
    try:
        a = int(input('Введите число:'))
        break
    except ValueError:
        print('Неверный ввод!!!')
if (math.factorial(a - 1) + 1) % a == 0:
    print('Простое')
else:
    print('Составное')
