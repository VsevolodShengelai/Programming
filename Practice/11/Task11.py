while True:
     try:
          a = input('Введите число:')
          b = int(a)
          d = int(a)
          n = input('Введите степень:')
          n = int(n)
          break
                  
     except ValueError:
         print('Неверный ввод!!!')

if n > 0 :
    for i in range(n-1):
        a = d * b
        d = a
elif n < 0:
    a = 1
    for i in range((-1)*n):
        a = a / b
elif n == 0:
    a = 1


print(a)
