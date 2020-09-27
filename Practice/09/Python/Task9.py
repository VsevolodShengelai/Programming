print('Введите два значения времени в виде часов и минут')
while True:
     try:
         
         s= input()
         if int( s[ : s.find(":")]) >= 0 and int( s[ : s.find(":")]) <= 23 and int(s[s.find(":") + 1 : ]) >= 0 and int(s[s.find(":") + 1 : ]) <= 59 :
             min1 = int(s[ : s.find(":")])*60+ int(s[s.find(":") + 1 : ])

         else:
             print('Введите корректные значения даты и времени')
             continue
         print(min1)

         q= input()
         if int( q[ : q.find(":")]) >= 0 and int( q[ : q.find(":")]) <= 23 and int(q[q.find(":") + 1 : ]) >= 0 and int(q[q.find(":") + 1 : ]) <= 59 :
             min1 = int(q[ : q.find(":")])*60+ int(q[q.find(":") + 1 : ])

         else:
             print('Введите корректные значения даты и времени')
             continue
         min2 = int(q[ : q.find(":")])*60+ int(q[q.find(":") + 1 : ])
         print(min2)

         break
                  
     except ValueError:
         print('Неверный ввод!!!')

if min2 - min1 <= 1:
    print('Встреча состоится')
else:
    print('Встреча не состоится')
