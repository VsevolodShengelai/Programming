from tkinter import *
from PIL import Image, ImageTk
import os
import json

root = Tk()
root.title("The last Quest")
root.geometry(str(9*35)+'x'+str(16*35))
root.resizable(width=False, height=False)

 #Нажали на изображение квеста
def Qbind(event):
    print('Запуск квеста!')

 #Блок загрузки изображений интерфейса и начального изменения их размеров
tileset = Image.open("Fon1-2.png")
BottomFonIMG = ImageTk.PhotoImage(tileset.crop((0, 0, tileset.size[0], 46)))
 
 ##Просмотр директории для выгрузки списка изображений квестов

def change(side):
    global current_quest
    global QuestIMG
    global current_img
    global BottomLabel
  
    if side == 'r':
        current_quest = current_quest+1
    else:
        current_quest = current_quest-1

    if current_quest > len(quest_images_list)-1:
        current_quest = 0
    elif current_quest < 0:
        current_quest = len(quest_images_list)-1
        
    print(current_quest)    
    print(quest_images_list[current_quest])
    current_img = 'Quest_images\\'+ quest_images_list[current_quest]
    QuestIMG = ImageTk.PhotoImage(file=current_img)
    TopLabel.configure(image = QuestIMG)
    Label_quest.configure(text = quest_images_list[current_quest][:len(quest_images_list[current_quest])-4])

def change_cuest_r():
    change('r')
def change_cuest_l():
    change('l')

 

path = "C:\Program Files (x86)\Python38-32\My programms\Quects_client\Quest_images"
print(os.listdir(path))
quest_images_list = os.listdir(path)
current_quest = 0
current_img = 'Quest_images\\'+ quest_images_list[current_quest]
QuestIMG = ImageTk.PhotoImage(file=current_img)

 ##Изображения для кнопок 
butt1IMG = ImageTk.PhotoImage(file='wheel.png')
butt2IMG = ImageTk.PhotoImage(file='medal.png')
butt3IMG = ImageTk.PhotoImage(file='kubok.png')
butt4IMG = ImageTk.PhotoImage(file='heart.png')
butt5IMG = ImageTk.PhotoImage(file='chest.png')


 # Область квестов
TopFrame = Frame(root, bg = 'snow3', highlightthickness = 0,
                     highlightcolor = 'SystemButtonFace',
                     height = 514, width = 315)
TopFrame.place(x = 0, y = 0)
TopLabel = Label(TopFrame, image = QuestIMG,
                    highlightthickness = 0, bd = 0)
TopLabel.place(x = 0, y = 0)
TopLabel.bind('<Button-1>', Qbind)


Button_right = Button(TopFrame, text = ">>", command = change_cuest_r)
Button_left = Button(TopFrame, text = "<<", command = change_cuest_l)


Button_right.place(x = 280, y = 480)
Button_left.place(x = 10, y = 480)
Label_quest = Label(width = 27,
                    text = quest_images_list[current_quest][:len(quest_images_list[current_quest])-4],
                    justify = CENTER)
Label_quest.place(x = 60, y = 480)
    
  ##Нижняя панель интрументов
BottomFrame = Frame(root, height = 46,
                     borderwidth = 0)
BottomFrame.place(x = 0, y = 514)

BottomLabel = Label(BottomFrame, image = BottomFonIMG,
                    highlightthickness = 0, bd = 0)
BottomLabel.pack()


Button1 = Button(BottomLabel, image = butt1IMG)
Button1.place(x = 10, y = 8)
Button2 = Button(BottomLabel, image = butt2IMG)
Button2.place(x = 50, y = 8)
Button3 = Button(BottomLabel, image = butt3IMG)
Button3.place(x = 110, y = 8)

GamePointsLabel = Label(BottomLabel, text ='10234',
                        highlightbackground = 'red',
                         highlightthickness = 7)
GamePointsLabel.place(x = 150, y = 8)

Button4 = Button(BottomLabel, image = butt4IMG)
Button4.place(x = 225, y = 8)
Button5 = Button(BottomLabel, image = butt5IMG)
Button5.place(x = 265, y = 8)



