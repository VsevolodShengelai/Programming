from tkinter import *
from tkinter.messagebox import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
import json
import Quest_viever
import Login_form
import Rating
import pygame
from os import path, chdir

root = Tk()
root.title("The last Quest")
root.geometry(str(11*35)+'x'+str(18*35))
root.resizable(width=False, height=False)

'''def server_request():
    r = requests.get('https://api.github.com').content.decode("UTF8")
    print(response.status_code)
    weather = json.loads(r)'''


 #Нажали на изображение квеста
def Qbind(event):
    print('Запуск квеста!')
    Quest_viever.init(root, list_of_cuests[current_quest], GamePointsLabel)

 #Блок загрузки изображений интерфейса и начального изменения их размеров
tileset = Image.open("Fon1-2.png")
BottomFonIMG = ImageTk.PhotoImage(tileset.crop((0, 0, tileset.size[0], 46)))

pygame.mixer.init()
def playmusic(nameof_current_quest):
    pygame.mixer.music.load("audio/"+nameof_current_quest+".mp3")        
    pygame.mixer.music.play(loops=-1)
    
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
    current_img = 'Quest_images\\'+ list_of_cuests[current_quest]+'.png'
    QuestIMG = ImageTk.PhotoImage(file=current_img)
    TopLabel.configure(image = QuestIMG)
    Label_quest.configure(text = list_of_cuests[current_quest])
    #Квесты перебираются по постерам, которые есть в наличии
    #Для получения имени срезаем .png
    nameof_current_quest = quest_images_list[current_quest][0:quest_images_list[current_quest].find('.')]
    print(nameof_current_quest)
    playmusic(nameof_current_quest)

def change_cuest_r():
    change('r')
def change_cuest_l():
    change('l')

 #Открываем и обрабатываем список текстовых квестов и открываем первый квест
 #То есть Просмотр директории для выгрузки списка изображений квестов
with open("config.json", "r") as read_file:
    config = json.load(read_file)
    list_of_cuests = config["list_of_downloaded_quests"]
    #print(list_of_cuests)
    read_file.close()

 ##Окрываем текущую директорию, в которой будем работать
abspath = path.abspath(__file__)
dirname = path.dirname(abspath)

path = dirname+"\Quest_images"
print(os.listdir(path))
quest_images_list = os.listdir(path)
current_quest = 0
current_img = 'Quest_images\\'+ list_of_cuests[current_quest]+'.png'
QuestIMG = ImageTk.PhotoImage(file=current_img)

 ##Изображения для кнопок 
butt1IMG = ImageTk.PhotoImage(file='wheel.png')
butt2IMG = ImageTk.PhotoImage(file='medal.png')
butt3IMG = ImageTk.PhotoImage(file='kubok.png')
butt4IMG = ImageTk.PhotoImage(file='heart.png')
butt5IMG = ImageTk.PhotoImage(file='chest.png')
butt6IMG = ImageTk.PhotoImage(file='back-button.png')

 # Область квестов
TopFrame = Frame(root, bg = 'snow3', highlightthickness = 0,
                     highlightcolor = 'SystemButtonFace',
                     height = 584, width = 385)
TopFrame.place(x = 0, y = 0)
TopLabel = Label(TopFrame, image = QuestIMG,
                    highlightthickness = 0, bd = 0)
TopLabel.place(x = 0, y = 0)
TopLabel.bind('<Button-1>', Qbind)

Button_right = Button(TopFrame, text = ">>", command = change_cuest_r)
Button_left = Button(TopFrame, text = "<<", command = change_cuest_l)
Button_right.place(x = 350, y = 550)
Button_left.place(x = 10, y = 550)

Label_quest = Label(width = 27,
                    text = quest_images_list[current_quest][:len(quest_images_list[current_quest])-4],
                    justify = CENTER)
Label_quest.place(x = 98, y = 550)
    
  ##Нижняя панель интрументов
BottomFrame = Frame(root, height = 46,
                     borderwidth = 0)
BottomFrame.place(x = 0, y = 584)

BottomLabel = Label(BottomFrame, image = BottomFonIMG,
                    highlightthickness = 0, bd = 0)
BottomLabel.pack()

# Картинки для магазина размещаем в глобальной области видиости
oko_gold_img = ImageTk.PhotoImage(file='Magazine\Gold-oko.png')
oko_simp_img = ImageTk.PhotoImage(file='Magazine\Simple-oko.png')
zakladka_gold_img = ImageTk.PhotoImage(file='Magazine\Gold-sakladka.png')
zakladka_simp_img = ImageTk.PhotoImage(file='Magazine\Simple-sakladka.png')

zakladka_60p_img = ImageTk.PhotoImage(file='Magazine\zakladka_60p.png')
oko_60p_img = ImageTk.PhotoImage(file='Magazine\oko_60p.png')

wallp_karta = ImageTk.PhotoImage(file='wallp_karta.png')


def open_shop():

    def destruct_shop():
        ShopFrame.destroy()
    
    def make_purchase(event):
        global config
        print(event.widget.name)

        answer = askyesno(
            title='Messagebox',
            message='Вы действительно хотите купить предмет?')
        if answer:
            print(config["value"])
            print(event.widget.cost)
            if config["value"] < event.widget.cost:
                showinfo(
                    title='Information',
                    message='Недостаточно валюты')
            else:
                showinfo(
                    title='Information',
                    message='Покупка совершена')
                if event.widget.name == 'oko-gold':
                    if config["items"]["oko"] != "INF":
                        config["items"]["oko"] = "INF"
                        config["value"] -= event.widget.cost
                elif event.widget.name == "oko-simple":
                    if config["items"]["oko"] != "INF":
                        config["items"]["oko"] += 3
                        config["value"] -= event.widget.cost
                if event.widget.name == 'zakladka-gold':
                    if config["items"]["zakladka"] != "INF":
                        config["items"]["zakladka"] = "INF"
                        config["value"] -= event.widget.cost
                elif event.widget.name == "zakladka-simple":
                    if config["items"]["zakladka"] != "INF":
                        config["items"]["zakladka"] += 2
                        config["value"] -= event.widget.cost
                
                with open('config.json', 'w') as file:
                    json.dump(config, file, indent=2, ensure_ascii=False)

        label_oko_NUM.configure(text = config["items"]["oko"])
        label_zakladka_NUM.configure(text = config["items"]["zakladka"])
        label_value_NUM.configure(text='Валюта: '+str(config["value"]))
                
        
    ShopFrame = Frame(root, bg = 'azure2', highlightthickness = 0,
                highlightcolor = 'SystemButtonFace',
                height = 584, width = 385)
    ShopFrame.place(x = 0, y = 0)
    ShopFrame.pack_propagate(False)

    oko_Num = config["items"]["oko"]
    zakladka_Num = config["items"]["zakladka"]
    
    Myitems=LabelFrame(ShopFrame, text= 'Имеющиеся предметы')
    label_oko = Label(Myitems, image = oko_60p_img)
    label_oko.pack(side = LEFT)
    label_oko_NUM = Label(Myitems, text = oko_Num)
    label_oko_NUM.pack(side = LEFT)

    separator = ttk.Separator(Myitems, orient='vertical')
    separator.pack(side = LEFT, fill = Y, padx = 30)
    
    label_zakladka = Label(Myitems, image = zakladka_60p_img)
    label_zakladka.pack(side = LEFT)
    label_zakladka_NUM = Label(Myitems, text = zakladka_Num)
    label_zakladka_NUM.pack(side = LEFT)
       
    Myitems.pack(fill = Y, pady=5, padx = 5)

    separator2 = ttk.Separator(Myitems, orient='vertical')
    separator2.pack(side = LEFT, fill = Y, padx = 30)

    label_value_NUM = Label(Myitems, text='Валюта: '+str(config["value"]))    
    label_value_NUM.pack(side = LEFT)
    
    Button_oko_gold = Button(ShopFrame, image = oko_gold_img,
                             relief=FLAT, bg = 'azure2')
    Button_oko_gold.name = 'oko-gold'
    Button_oko_gold.cost = 5000
    Button_oko_gold.bind('<Button-1>', make_purchase)
    Button_oko_gold.pack(pady=5)

    Button_oko_simple = Button(ShopFrame, image = oko_simp_img,
                             relief=FLAT, bg = 'azure2')
    Button_oko_simple.name = 'oko-simple'
    Button_oko_simple.cost = 90
    Button_oko_simple.bind('<Button-1>', make_purchase)
    Button_oko_simple.pack(pady=5)

    Button_zakladka_gold = Button(ShopFrame, image = zakladka_gold_img,
                             relief=FLAT, bg = 'azure2')
    Button_zakladka_gold.name = 'zakladka-gold'
    Button_zakladka_gold.cost = 4000
    Button_zakladka_gold.bind('<Button-1>', make_purchase)
    Button_zakladka_gold.pack(pady=5)

    Button_zakladka_simple = Button(ShopFrame, image = zakladka_simp_img,
                             relief=FLAT, bg = 'azure2')
    Button_zakladka_simple.name = 'zakladka-simple'
    Button_zakladka_simple.cost = 80
    Button_zakladka_simple.bind('<Button-1>', make_purchase)
    Button_zakladka_simple.pack(pady=5)

    Button6.configure(command = destruct_shop)

def setup():
    def destruct_setup():
        SetupFrame.destroy()
    def register():
        Login_form.init(root)
        if config["Registered"] == "YES":
            with open("clear-config.json", "r") as read_file:
                clearconfig = json.load(read_file)
            read_file.close()

            with open('config.json', 'w') as read_file:
                json.dump(clearconfig, read_file, indent=2, ensure_ascii=False)
            read_file.close()
            

    SetupFrame = Frame(root, bg = 'azure2', highlightthickness = 0,
                highlightcolor = 'SystemButtonFace',
                height = 584, width = 385)
    SetupFrame.place(x = 0, y = 0)
    SetupFrame.pack_propagate(False)
    
    ThemeLabel = Label(SetupFrame, image = wallp_karta, height = 584, width = 385)
    ThemeLabel.pack()
    ThemeLabel.pack_propagate(False)

    with open("config.json", "r") as read_file:
        config = json.load(read_file)
    read_file.close()

    if config["Registered"] == "NO":
        Register_but_text = 'Регистрация/Вход'
    else:
        Register_but_text = 'Выйти'
        
    Register_but = Button(ThemeLabel, text = Register_but_text, bg = 'coral',
                         font=("Helvetica", "12"), command = register)
    Register_but.pack()

    Button6.configure(command = destruct_setup)

def rating():
    Rating.init(root)

#Нижняя панель кнопок
    
Button1 = Button(BottomLabel, image = butt1IMG, command = setup)
Button1.place(x = 10, y = 8)
Button2 = Button(BottomLabel, image = butt2IMG)
Button2.place(x = 50, y = 8)
Button3 = Button(BottomLabel, image = butt3IMG)
Button3.place(x = 110, y = 8)

GamePointsLabel = Label(BottomLabel, text = config['globalscores'],
                        highlightbackground = 'red',
                         highlightthickness = 7, width = 7)
GamePointsLabel.place(x = 150, y = 8)

Button4 = Button(BottomLabel, image = butt4IMG)
Button4.place(x = 225, y = 8)
Button5 = Button(BottomLabel, image = butt5IMG, command = open_shop)
Button5.place(x = 265, y = 8)

Button6 = Button(BottomLabel, image = butt6IMG)
Button6.place(x = 325, y = 8)


## Поиск файла config.json и создание лог. переменной

if config["Registered"] == "NO":
    Login_form.init(root)
else:
    print('Файл config.json не обнаружен!')


