def get_ints():
 while True:
     try:
         a = input('X: ')

         for  i in a:
             if i == '.':
                 a = float(a)
         if type(a) != float:
            a = int(a)

         b = input('Y: ')

         for  i in b:
             if i == '.':
                 b = float(b)
         if type(b) != float:
              b = int(b)
         return a, b
     except ValueError:
         print('Неверный ввод!!!')
 
 
a, b = get_ints()


print ('Переменные a и b приняли следующие значения:')
print ('a = ', a, '\n', 'b = ', b, sep="")

print ('Обменяем a и b значениями с помощью дополнительной переменной:')
c = a
a = b
b = c       
print ('a = ', a, '\n', 'b = ', b, sep="")

print ('Обменяем a и b значениями с БЕЗ помощи дополнительной переменной:')
a, b = b, a      
print ('a = ', a, '\n', 'b = ', b, sep="")

