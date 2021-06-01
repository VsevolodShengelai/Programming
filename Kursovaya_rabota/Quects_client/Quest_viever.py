#Здесь в дальнейшем стоит взять только те кkассы, которые имеют значение
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import json
from PIL import Image, ImageTk
from tkinter import ttk
from functools import partial
from tkinter import scrolledtext

endstatus = 'None'

current_part = 'part1'
zakladka = None 

with open("config.json", "r") as read_file:
    config = json.load(read_file)

def init(root, cuest_name, GamePointsLabel):
    MainFrame = Frame(root, bg = 'snow3', highlightthickness = 0,
                     highlightcolor = 'DarkGoldenrod3',
                     height = 584, width = 385)
    MainFrame.place(x = 0, y = 0)
    MainFrame.pack_propagate(False)

    qpath = "Quest_text\\" + cuest_name + ".json"

    with open(qpath, "r") as read_file:
        quest = json.load(read_file)
        print(quest)
        
    print(list(quest))

    buttonlist = []
   

    def destroy():
        MainFrame.destroy()

    def startquest(name):
        chaptername=name
        print(chaptername + ' is start!!!')
        #print(quest['book'][chaptername])

        def destroy():
            CuestFieldFrame.destroy()

        def endof_cuest(event):
            destroy()
            scores = quest['Description']['scores']
            print(scores)
            ## Добавляем очки за квест, если квест завершился удачно
            if endstatus == "GOOD":
                with open('config.json', 'r') as file:
                    json_data = json.load(file)
                    i=0
                    for item in json_data['list of scores']:
                        print(item)
                        print(list(item.keys())[0])

                        if cuest_name == list(item.keys())[0]:
                            if json_data['list of scores'][i][list(item.keys())[0]] == 'NO':
                                json_data['list of scores'][i][list(item.keys())[0]] = 'YES'
                                json_data['globalscores'] += scores
                                #print(json_data)
                                with open('config.json', 'w') as file:
                                    json.dump(json_data, file, indent=2, ensure_ascii=False)                     
                        GamePointsLabel.config(text=json_data['globalscores'])
                        i+=1    

        # Меняет список кнокок-действий в квесте (и добавляет новый фрагмент текста)         
        def Change_buttons(part):

            ## Сначала убираем старые кнопки-действия
            for widget in myframe2.winfo_children():
                widget.destroy()
                 

            for i in range(len(quest['book'][chaptername][part]['buttons'])):
                
                btn = Button(myframe2,
                         text=quest['book'][chaptername][part]['buttons']['button'+str(i+1)]['name'],
                         font=('Helvetica', '12'))
                btn.goto = quest['book'][chaptername][part]['buttons']['button'+str(i+1)]['goto']
                btn.text = quest['book'][chaptername][part]['buttons']['button'+str(i+1)]['name']

                if 'end' in list(quest['book'][chaptername][part]['buttons']['button'+str(i+1)].keys()):
                    print(quest['book'][chaptername][part]['buttons']['button'+str(i+1)]['end'])
                    global endstatus
                    endstatus = quest['book'][chaptername][part]['buttons']['button'+str(i+1)]['end']
                    btn.bind('<Button-1>', endof_cuest)
                    
                else:
                    btn.bind('<Button-1>', changepart)
            
                buttonlist.append(btn)
                btn.pack(pady=2)
             ##Втавялем следующий текстовый фрагмент
            global current_part 
            current_part = part #Это нужно для Ока
            #print(current_part)
            text_of_quest.insert(END, quest['book'][chaptername][part]['text'])

            
        def changepart(event):
            #print(event.widget.goto)
            text_of_quest.insert(END, '\n'+'\n'+'//'+event.widget.text+'\n'+'\n')
            buttonlist = []
            Change_buttons(event.widget.goto)

        def use_oko():
            def execute_algorithm():
                    global config 
                    with open('config.json', 'w') as file:
                        json.dump(config, file, indent=2, ensure_ascii=False)                   
                    label_oko_NUM.configure(text = config["items"]["oko"])
                    
                    text_of_quest.insert(END, '\n\n==Вы использоали Око!==')
                    
                    for i in range(len(quest['book'][chaptername][current_part]['buttons'])):
                        text_of_quest.insert(END, '\n[Око]>>'+quest['book'][chaptername][current_part]['buttons']['button'+str(i+1)]['name'])
                        where_we_go = quest['book'][chaptername][current_part]['buttons']['button'+str(i+1)]['goto']
                        text_of_quest.insert(END,'\n\n'+quest['book'][chaptername][where_we_go]['text'])
                        text_of_quest.insert(END,'\n==Все концовки были освещены==')              

            if config["items"]["oko"] != "INF":
                if config["items"]["oko"] > 0:
                    config["items"]["oko"] -= 1
                    execute_algorithm()
            if config["items"]["oko"] == "INF":
                execute_algorithm()
                
        def place_zakladka():
            global zakladka
            if config["items"]["zakladka"] != "INF":
                if config["items"]["zakladka"] > 0:
                    config["items"]["zakladka"] -= 1
                    zakladka = current_part
                    label_zakladka_NUM.configure(text = config["items"]["zakladka"])
            if config["items"]["zakladka"] == "INF":
                zakladka = current_part
                label_oko_NUM.configure(text = config["items"]["zakladka"])

        def use_zakladka():
            #print(zakladka)
            text_of_quest.insert(END,'\n\n==Возвращение к закладке==\n\n')
            Change_buttons(zakladka)

                    

        CuestFieldFrame = Frame(root, bg = 'snow3', highlightthickness = 0,
                     highlightcolor = 'SystemButtonFace',
                     height = 584, width = 385)
        CuestFieldFrame.place(x = 0, y = 0)
        CuestFieldFrame.pack_propagate(False)

        wrapper1 = LabelFrame(CuestFieldFrame)
        wrapper2 = LabelFrame(CuestFieldFrame, height=60)

        #Поле особых фишек
        
        oko_Num = config["items"]["oko"]
        zakladka_Num = config["items"]["zakladka"]

        Myitems=LabelFrame(wrapper1, text= 'Предметы')
        
        label_oko = Button(Myitems, image = oko_30p_img, command = use_oko)
        label_oko.pack(side = LEFT)
        label_oko_NUM = Label(Myitems, text = oko_Num)
        label_oko_NUM.pack(side = LEFT)

        separator = ttk.Separator(Myitems, orient='vertical')
        separator.pack(side = LEFT, fill = Y, padx = 8)
    
        label_zakladka = Button(Myitems, image = zakladka_30p_img, command = place_zakladka)
        label_zakladka.pack(side = LEFT)
        label_zakladka_NUM = Label(Myitems, text = zakladka_Num)
        label_zakladka_NUM.pack(side = LEFT)

        label_empty = Label(Myitems)
        label_empty.pack(side = LEFT, padx = 36)

        label_zakladka = Button(Myitems, text = 'Вернуться к закладке',
                                command = use_zakladka)
        label_zakladka.pack(side = LEFT)
        
        Myitems.pack(fill = Y, pady=5, padx = 5)

        #Первый скроллбар
         ##Это текстовый виджет с уже встроенным скроллбаром
        text_of_quest = scrolledtext.ScrolledText(wrapper1,wrap=WORD, width = 42)
          ##Вставим первый фрагмент текста
        text_of_quest.insert(END, quest['book'][chaptername]['part1']['text'])
        text_of_quest.pack()

        

        #Второй скроллбар
        mycanvas2 = Canvas(wrapper2, width = 341)
        mycanvas2.pack(side=LEFT, fill="both", expand=1)
 
        yscrollbar2= ttk.Scrollbar(wrapper2, orient="vertical", command=mycanvas2.yview)
        yscrollbar2.pack(side=RIGHT, fill="y")

        mycanvas2.configure(yscrollcommand=yscrollbar2.set)

        mycanvas2.bind('<Configure>', lambda e: mycanvas2.configure(scrollregion=mycanvas2.bbox('all')))

        myframe2 = Frame(mycanvas2)
        mycanvas2.create_window((0,0), window=myframe2, anchor='nw')   

        wrapper1.pack(fill="y", padx=2, pady=2)
        wrapper2.pack(fill="y", padx=2, pady=2)

                
        for i in range(len(quest['book'][chaptername]['part1']['buttons'])):

            btn = Button(myframe2,
                         text=quest['book'][chaptername]['part1']['buttons']['button'+str(i+1)]['name'],
                         font=('Helvetica', '12'))
            btn.goto = quest['book'][chaptername]['part1']['buttons']['button'+str(i+1)]['goto']
            btn.text = quest['book'][chaptername]['part1']['buttons']['button'+str(i+1)]['name']
           
            btn.bind('<Button-1>', changepart)
            
            buttonlist.append(btn)
            btn.pack(pady=2)
      
        w2But=Button(CuestFieldFrame, text='Назад', command = destroy)
        w2But.pack(side=BOTTOM, padx=2, pady=2)

        

    def show_list_of_chapters():
        wrapper1 = LabelFrame(MainFrame)
        wrapper2 = LabelFrame(MainFrame, height=60)


        mycanvas = Canvas(wrapper1, width = 341)
        mycanvas.pack(side=LEFT, fill="both", expand=1)
 
        yscrollbar= ttk.Scrollbar(wrapper1, orient="vertical", command=mycanvas.yview)
        yscrollbar.pack(side=RIGHT, fill="y")

        mycanvas.configure(yscrollcommand=yscrollbar.set)

        mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion=mycanvas.bbox('all')))

        myframe = Frame(mycanvas)
        mycanvas.create_window((0,0), window=myframe, anchor='nw')

        w2But=Button(wrapper2, text='Назад', command = destroy)
        w2But.pack()

        wrapper1.pack(fill="both", expand="yes", padx=10, pady=10)
        wrapper2.pack(fill="both", padx=10, pady=10)
   
        for i in range(len(quest['book'])):

            btn = Button(myframe, text=list(quest['book'])[i],
                         font=('Helvetica', '14'),
                         command=partial(startquest, list(quest['book'])[i]))

            buttonlist.append(btn)
            btn.pack(pady=2)

    zakladka_30p_img = ImageTk.PhotoImage(file='Magazine\zakladka_30p.png')
    oko_30p_img = ImageTk.PhotoImage(file='Magazine\oko_30p.png')
                         
    show_list_of_chapters()
