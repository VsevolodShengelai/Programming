print('Введите значения переменных a и b через пробел')
a, b = input().split(' ')

for  i in a:
    if i == '.':
        a = float(a)
if type(a) != float:
    a = int(a)

 
for  i in b:
    if i == '.':
        b = float(b)
if type(b) != float:
    b = int(b)


print('a+b =', a+b)
print('a-b =', a-b)
print('a*b =', a*b)
print('a/b =', a/b)
    
