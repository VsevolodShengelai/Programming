#Программа нахождения площади треугольника

import math
#Проверка на дурака
def get_mode():
 while True:
     try:
         mode = input('mode = ')
         mode = int(mode)
         if mode != 1 and mode != 2:
             print('Выберите режим ("1" или "2")')
             mode = get_mode()
         return mode

     except ValueError:
         print('Неверный ввод!!!')

def get_ints():
 while True:
     try:

         a = input('a = ')
         a = float(a)


         b = input('b = ')
         b = float(b)
         
         c = input('c = ')
         c = float(c)

         return a, b, c

     except ValueError:
         print('Неверный ввод!!!')

def get_coord():
 while True:
     try:
         x,y = input().split()
         x = float(x)
         y = float(y)
         return x, y

     except ValueError:
         print('Неверный ввод!!!')


print('Выберите способ нахождения площади треугольника ("1" или "2")')
print()
print('"1"- Через длины сторон')
print('"2"- Через координаты вершин')
print()
print('Затем введите требуемые значения')

mode = get_mode()

while True:
 if mode == 1:
    a, b, c = get_ints()

    if a + b < c or a + c < b or b + c < a:
        print('Треугольник не существует')
        continue

    p = (a+b+c)/2
    S = math.sqrt (p*(p-a)*(p-b)*(p-c))
    print('S = ',S)
    break

 else:
    print('Введите координаты вершин')
    x1,y1 = get_coord()
    x2,y2 = get_coord()
    x3,y3 = get_coord()
    a = math.sqrt(math.pow((x1-x2),2)+math.pow((y1-y2),2))
    b = math.sqrt(math.pow((x1-x3),2)+math.pow((y1-y3),2))
    c = math.sqrt(math.pow((x2-x3),2)+math.pow((y2-y3),2))

    if a + b < c or a + c < b or b + c < a:
        print('Треугольник не существует')
        continue

    p = (a+b+c)/2
    S = math.sqrt (p*(p-a)*(p-b)*(p-c))
    print('S = ',S)
    break

