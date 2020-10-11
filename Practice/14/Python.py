
while True:
    try:
        n = int(input('Введите число n в пределах (0<=n<=10¹⁵):'))
        break
        if n < 0:
            print('Неверный ввод!')
            continue
    except ValueError:
        print('Неверный ввод!')


count = 0 
x = 1
if n == 0:
     print(0)
else:
   while x <= n:
       x = x * 2
       count += 1
   print(count)


