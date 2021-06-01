from tkinter import *
import requests
import json

def init(root):

    def destroy():
        LoginFrame.destroy()


    basepady = 8
    
    def register():

        def clicked():
            if password_entry.get() != '' and password_entry2.get() != '':
                if password_entry.get() == password_entry2.get():
                    #print(password_entry.get(), password_entry2.get())
                    url = 'http://localhost:1234/'
                    print(url)

                    with open("config.json", "r") as read_file:
                            config = json.load(read_file)
                    read_file.close()
                    user = username_entry.get()
                    pasw = password_entry.get()
                    
                    print(config)
                    payload = {'login': username_entry.get(), 'password': password_entry.get(), 'config': str(config)}

                    r = requests.get(url, payload)

                    if r.status_code == 200:
                        print('Success!')
                        print(r.content.decode("UTF8"))

                        if r.content.decode("UTF8") == 'NO':
                            status_label.configure(text= 'Пользователь с таким именем уже существует')
                        elif r.content.decode("UTF8") == 'None':
                            status_label.configure(text= 'Пользователь с таким именем уже существует')
                        else:
                            status_label.configure(text= 'Регистрация прошла успешно')
                            destroy()
                            
                            with open("config.json", "r") as read_file:
                                config = json.load(read_file)
                            read_file.close()

                            config["Registered"] = "YES"
                            config["Password"] = pasw
                            config["Username"] = user

                            with open('config.json', 'w') as file:
                                json.dump(config, file, indent=2, ensure_ascii=False)
                            file.close()
                else:
                    status_label.configure(text= 'Введённые пароли не совпадают')
                            
                            
        destroy()

        global LoginFrame
        LoginFrame = Frame(root, bg = 'SpringGreen', height = 630, width = 385)
        LoginFrame.place(x = 0, y = 0)
        LoginFrame.pack_propagate(False)
        
        #Метка для добавления отступа перед блоком регистрации
        StructureLabel = Label(LoginFrame, font = ('Arial', 15),
                     bg = 'SpringGreen')
        StructureLabel.pack(pady=20)
    
        #заголовок формы
        main_label = Label(LoginFrame, text = 'Войти', font = ('Arial', 15),
                     bg = 'SpringGreen')
        main_label.pack()

        #метка для поля ввода имени
        username_label = Label(LoginFrame, text = 'Имя пользователя', font = ('Arial', 10),
                     bg = 'SpringGreen', pady = basepady)
        username_label.pack()

        #поле ввода имени
        username_entry = Entry(LoginFrame, bg='#fff', fg='#444', font=('Arial', 10))
        username_entry.pack()

        #метка для поля ввода пароля
        password_label = Label(LoginFrame, bg = 'SpringGreen', text='Пароль', font=('Arial', 10),
                           pady = basepady)
        password_label.pack()

        # поле ввода пароля
        password_entry = Entry(LoginFrame, bg='#fff', fg='#444', font=('Arial', 10))
        password_entry.pack()

        #метка для поля ввода пароля_2
        password_label = Label(LoginFrame, bg = 'SpringGreen', text='Повторите Пароль', font=('Arial', 10),
                           pady = basepady)
        password_label.pack()

        # поле ввода пароля_2
        password_entry2 = Entry(LoginFrame, bg='#fff', fg='#444', font=('Arial', 10))
        password_entry2.pack()

        # кнопка отправки формы
        send_btn = Button(LoginFrame, bg = 'SpringGreen', text='Зарегистрироваться', command=clicked)
        send_btn.pack(pady = basepady)

        #статус ввода
        status_label = Label(LoginFrame, text = 'статус', font = ('Arial', 10),
                     bg = 'SpringGreen')
        status_label.pack()

        #Другие кнопки
        OtherButtFrame = Frame(LoginFrame, bg = 'SpringGreen')
        OtherButtFrame.pack(pady = 20)
        regibut = Button(LoginFrame, bg = 'SpringGreen2', text='Войти', width = 18, command = enter)
        regibut.pack(pady = 2)
        guestbut = Button(LoginFrame, bg = 'medium spring green', text='Играть локально', width = 18,
                      command = destroy)
        guestbut.pack(pady = 2)

    def enter():

        def clicked():
            if password_entry.get() != '':
                if password_entry.get():
                    url = 'http://localhost:1234/enter'
                    print(url)

                    with open("config.json", "r") as read_file:
                            config = json.load(read_file)
                            read_file.close()
                    payload = {'login': username_entry.get(), 'password': password_entry.get()}
                    #print(payload)

                    r = requests.get(url, payload)

                    if r.status_code == 200:
                        print('Success!')
                        print(r.content.decode("UTF8"))

                        if r.content.decode("UTF8") == 'None':
                            status_label.configure(text= "Такого аккаунта нет")
                        else:
                            #x = json.loads(r.content.decode("UTF8"))#Превращаем json в строку
                            #y = json.dumps(r.content.decode("UTF8")) #Загружаем json
                            #print(y['Registered'])
                            list_1 = ''
                            list_ = r.content.decode("UTF8")
                            for literal in list_:
                                if literal == "\'":
                                    list_1 += "\""
                                else:
                                    list_1 += literal
                            print(list_1)
                                                  
                            x = json.loads(list_1)

                            with open('config.json', 'w') as file:
                                json.dump(x, file, indent=2, ensure_ascii=False)
                            read_file.close()

                            with open("config.json", "r") as read_file:
                                config = json.load(read_file)
                                config["Registered"] = "YES"
                            read_file.close()

                            with open('config.json', 'w') as file:
                                json.dump(config, file, indent=2, ensure_ascii=False)
                            read_file.close()
                            destroy()

                            

        if 'lLoginFrame' in globals():
            destroy()

        global LoginFrame
        LoginFrame = Frame(root, bg = 'SpringGreen', height = 630, width = 385)
        LoginFrame.place(x = 0, y = 0)
        LoginFrame.pack_propagate(False)   

        #Метка для добавления отступа перед блоком регистрации
        StructureLabel = Label(LoginFrame, font = ('Arial', 15),
                     bg = 'SpringGreen')
        StructureLabel.pack(pady=20)
    
        #заголовок формы
        main_label = Label(LoginFrame, text = 'Войти', font = ('Arial', 15),
                     bg = 'SpringGreen')
        main_label.pack()

        #метка для поля ввода имени
        username_label = Label(LoginFrame, text = 'Имя пользователя', font = ('Arial', 10),
                     bg = 'SpringGreen', pady = basepady)
        username_label.pack()

        #поле ввода имени
        username_entry = Entry(LoginFrame, bg='#fff', fg='#444', font=('Arial', 10))
        username_entry.pack()

        #метка для поля ввода пароля
        password_label = Label(LoginFrame, bg = 'SpringGreen', text='Пароль', font=('Arial', 10),
                           pady = basepady)
        password_label.pack()

        # поле ввода пароля
        password_entry = Entry(LoginFrame, bg='#fff', fg='#444', font=('Arial', 10))
        password_entry.pack()

        # кнопка отправки формы
        send_btn = Button(LoginFrame, bg = 'SpringGreen', text='Войти', command = clicked)
        send_btn.pack(pady = basepady)

        #статус ввода
        status_label = Label(LoginFrame, text = 'статус', font = ('Arial', 10),
                     bg = 'SpringGreen')
        status_label.pack()

        #Другие кнопки
        OtherButtFrame = Frame(LoginFrame, bg = 'SpringGreen')
        OtherButtFrame.pack(pady = 20)
        regibut = Button(LoginFrame, bg = 'SpringGreen2', text='Зарегистрироваться', width = 18, command = register)
        regibut.pack(pady = 2)
        guestbut = Button(LoginFrame, bg = 'medium spring green', text='Играть локально', width = 18,
                      command = destroy)
        guestbut.pack(pady = 2)

    enter()
    
    

