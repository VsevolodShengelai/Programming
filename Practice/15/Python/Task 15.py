# Это игра по угадыванию чисел.
import random
import time

def playAGame():
 guessesTaken = 0



 number = random.randint(1, 100)
 print('Здравствуйте. Это игра "Угадай число".')
 time.sleep(0.8)
 print('Что ж, я загадываю число от 1 до 100.')
 time.sleep(0.8)
 print('Попробуйте угадать.')
 for guessesTaken in range(6):
     
     guess = input()
     guess = int(guess)

     if guess < number:
         print('Загаданное число меньше')

     if guess > number:
         print('Загаданное число больше')

     if guess == number:
         break

 if guess == number:
     guessesTaken = str(guessesTaken + 1)
     print('Поздравляю! Вы угадали за ' + guessesTaken + ' попытки!')

 if guess != number:
     number = str(number)
     print('Вы проиграли. Было загадано: ' + number + '.')

playAGame()
print('"Хотите начать сначала? (1 - ДА )')
newgame = int(input())
if newgame == 1:
    playAGame()

    
