#Проверка на дурака
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

print('Решаем уравнение a•x²+b•x+c=0')

a, b, c = get_ints()


if a == 0:
    if b == 0:
        if c == 0:
            print('x = Любое число')
        else:
            print('Уравнение не имеет решений')
    else:
        print('x = ' + str(-c/b))
else:
    if b == 0:
        if c == 0:
            print('x = 0')
        else:
            X2= c/a
            if X2 < 0:
                print('Действительных корней нет')
            else:
                print('x = ' + str(X2 ** 0.52))
    else:
        if c == 0:
            print('x1 = 0')    
            print('x2 = ' + str(-b/a))
        else:
            D = b**2 - 4*a*c
            print('Дискриминант = ' + str(D))
            if D < 0:
                print('Действительных корней нет')
            elif D == 0:
                x = -b / (2 * a)
                print('x = ' + str(x))
            else:
                x1 = (-b + D ** 0.5) / (2 * a)
                x2 = (-b - D ** 0.5) / (2 * a)
                print('x1 = ' + str(x1))
                print('x2 = ' + str(x2))
  



  
