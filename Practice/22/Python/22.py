import sys

maze = [
    "####B######################",
    "# #       #   #      #    #",
    "# # # ###### #### ####### #",
    "# # # #       #   #       #",
    "#   # # ######### # ##### #",
    "# # # #   #       #     # #",
    "### ### ### ############# #",
    "# #   #     # #           #",
    "# # #   ####### ###########",
    "# # # #       # #         C",
    "# # ##### ### # # ####### #",
    "# # #     ### # #       # #",
    "#   ##### ### # ######### #",
    "######### ### #           #",
    "# ####### ### #############",
    "A           #   ###   #   #",
    "# ############# ### # # # #",
    "# ###       # # ### # # # #",
    "# ######### # # ### # # # F",
    "#       ### # #     # # # #",
    "# ######### # ##### # # # #",
    "# #######   #       #   # #",
    "# ####### ######### #######",
    "#         #########       #",
    "#######E############D######"
]




def MakeMatrix(maze):
    Matrix = []
    lst = []
    for i in range(len(maze)):
       lst = list(maze[i])

       Matrix.append(lst)

    # Выведу все элементы матрицы для себя

    for i in range ( len(Matrix) ): 
      for j in range ( len(Matrix[i]) ): 
          print ( Matrix[i][j], end = "" ) 
      print ('')
    print ('')
    return Matrix

def isOnBoard(x, y, Matrix):
    # Вернуть True, если координаты есть на игровом поле.
    return x >= 0 and x < len(Matrix) and y >= 0 and y < len(Matrix[x])

def getPlayerMove(Matrix):
    # Позволить игроку ввести свой ход.
    # Вернуть ход.

    while True:
        print('Укажите ход')
        y, x  = input().split()
        x = int(x)
        y = int(y)
        if Matrix [x][y] == ' ' and isOnBoard(x, y, Matrix):
            print('Нормальные координаты')
            flag = 1
            return x, y, flag
        else:
            print('Не верные координаты')
            flag = 0
            return x, y, flag

def MakeMove(x, y):
        global Previos
    
        for xdirection, ydirection in [[0, 1], [1, 0], [0, -1], [-1, 0]]:

            x1 = x + xdirection # Первый шаг в направлении x
            y1 = y + ydirection # Первый шаг в направлении y

            #Фича для разраба
            #print([x1,y1],Matrix[x1][y1])

            if isOnBoard(x1, y1, Matrix) and [x1,y1] not in Previos:
                if Matrix[x1][y1] != '#':
                    if Matrix[x1][y1] != ' ':
                        Exit.append(Matrix[x1][y1])
                        Previos.append([x1,y1])
                    else:
                        Previos.append([x1,y1])
                        #cuteCOORD.append([x1,y1])
                        MakeMove(x1, y1)



Matrix = MakeMatrix(maze)

x, y, flag = getPlayerMove(Matrix)
if flag == 0:
    sys.exit()

print('Размер матрицы:',len(Matrix),'строк', len(Matrix[x]),'столбцов\n')
print(Matrix[2][1])

Exit = []
Previos = []
#cuteCOORD = []

MakeMove(x, y)

for i in Exit: print(i,' ',end = '')
