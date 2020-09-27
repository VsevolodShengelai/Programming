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




print('a+b =', a+b)
print('a-b =', a-b)
print('a*b =', a*b)
print('a/b =', a/b)
    
