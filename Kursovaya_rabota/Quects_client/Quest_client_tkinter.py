from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("The last Quest")
root.geometry(str(9*35)+'x'+str(16*35))
root.resizable(width=False, height=False)

#Блок загрузки изображений интерфейса и начального изменения их размеров
tileset = Image.open("Fon1-1.png")
BottomFonIMG = ImageTk.PhotoImage(tileset.crop((0, 0, tileset.size[0], 46)))

 ##Изображения для кнопок
butt1IMG = ImageTk.PhotoImage(file='wheel.png')
butt2IMG = ImageTk.PhotoImage(file='medal.png')
butt3IMG = ImageTk.PhotoImage(file='kubok.png')
butt4IMG = ImageTk.PhotoImage(file='heart.png')
butt5IMG = ImageTk.PhotoImage(file='chest.png')


TopFrame = Frame(root, bg = 'snow3', highlightthickness = 5,
                     highlightcolor = 'SystemButtonFace')
TopFrame.pack(fill = BOTH, expand=1)

    
BottomFrame = Frame(root, height = 46,
                     borderwidth = 0)
BottomFrame.pack(expand=0)

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


'''Label1 = Label(BottomFrame, image = Label1IMG)
Label1.place(x = 0, y = 0)'''



