def get_ints():
 while True:
     try:

         x0, v0, t = input('Введите значение следующих переменных: \n * Начальное значение координаты\n * Начальную скорость\n * Время полёта \n').split()

         for i in x0:
             if i == '.':
                 x0 = float(x0)
         if type(x0) != float:
            x0 = int(x0)


         for  i in v0:
             if i == '.':
                 v0 = float(v0)
         if type(v0) != float:
            v0 = int(v0)
         

         for  i in t:
             if i == '.':
                 t = float(t)
         if type(t) != float:
            t = int(t)

         return x0, v0, t

     except ValueError:
         print('Неверный ввод!!!')
 
 
x0, v0, t = get_ints()

x = x0 + v0 * t - 9.8 * t * t/2

print('Расстояние до начальной точки:', x)
