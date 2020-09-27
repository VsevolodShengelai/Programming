print('#Калькулятор#')
print('Чтобы прекратить действие программы, введите "Стоп" ')
print('Введите выражение:')

while True:
     try:
         a = input()
         if a == 'Стоп':
             break        
         print(eval(a))

     except ValueError :
         print('Неверный ввод!!!')
     except NameError:
         print('Неверный ввод!!!')
     except SyntaxError:
         print('Неверный ввод!!!')
