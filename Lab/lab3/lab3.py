from tkinter import *

import math

from PIL import ImageTk, Image 

root = Tk()
root.title("")

images_balls = {
        
        "ball-red": Image.open("img/ball-red.png").convert('RGBA'),

        "ball-green": Image.open("img/ball-green.png").convert('RGBA'),
   
        "ball-violet": Image.open("img/ball-violet.png").convert('RGBA')        
}
back = PhotoImage(file="damaged_metal_orig.2.png")
interface =PhotoImage(file="imgonline-com-ua-Resize-RbmtiTZkMPDM.png")

cell_bg = Image.open("img/cell-bgr.png").convert('RGBA')

cell_bg.paste(images_balls["ball-green"] ,   # Накладываемая картинка
          (5,5),  # Сместить картинку на (x, y) пикселей
          images_balls["ball-green"] )
cell_bg = ImageTk.PhotoImage(cell_bg)



#Описание полотна для пульта управления
canvas2 = Canvas(root, width = 600, height = 600,
                bg = 'blue', bd = 0,
                borderwidth = 0,
                highlightthickness = 0) 
canvas2.grid(row=0, column=0, pady=0)
canvas2.create_image(0, 0, image = interface, anchor = NW)

#Это Canvas для самой игры
canvas = Canvas(root, width = 250, height = 600,
                bg = 'blue', bd = 0,
                borderwidth = 0,
                highlightthickness = 0) 
canvas.grid(row=0, column=1, pady=0)
canvas.create_image(0, 0, image = back, anchor = NW)



start_x = 12
start_y = 12

for row in range(9):
    for col in range(9):
        lbl = Label(canvas2,
                    text=', '.join([str(row), str(col)]),
                    bg="sky blue", 
                    borderwidth = 0, image = cell_bg)


        if col < 8:
            
            lbl_window = canvas2.create_window(start_x, start_y, anchor=NW, window=lbl)
            start_x += 65
            
        if col == 8:
            
            lbl_window = canvas2.create_window(start_x, start_y, anchor=NW, window=lbl)
            start_x = 10
            start_y += 65

'''lbl = Label(canvas2,
    
    bg="sky blue", 
    borderwidth = 2, image = img, )           
lbl_window = canvas2.create_window(start_x, start_y, anchor=NW, window=lbl)'''

#menu

canvas.create_text(14, 40, text="Линии 2",
                   font=("Arial", 18), fill="white", anchor=W)
canvas.create_text(14, 80, text="Счёт: 0",
                   font=("Arial", 18), fill="white", anchor=W)
Makemove_Button = Button(canvas, text='Сделать ход', font=("Arial", 12), fg='white', bg='#666666', activebackground='#777777',
           activeforeground='white')
Makemove_Button_window = canvas.create_window(14, 120, anchor=NW, window=Makemove_Button )

canvas.create_text(14, 180, text="Подсказка:", font=("Arial", 15), fill="#888888", anchor=NW)

NewgameButton = Button(canvas, text='Новая игра', font=("Arial", 12), fg='white', bg='#666666', activebackground='#777777',
        activeforeground='white')
NewgameButton_window = canvas.create_window(14, 300, anchor=NW, window=NewgameButton)

root.mainloop()
    
    
