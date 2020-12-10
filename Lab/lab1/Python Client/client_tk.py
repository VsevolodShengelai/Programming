from tkinter import *
import json
import requests

#Глобальный объект на основе класса Tk
root = Tk()

def WeatherReload(event=None):
	r = requests.get('http://localhost:3000/raw').content.decode("UTF8")
	weather = json.loads(r)
	description.config(text='Симферополь\n'+str(weather["description"]))
	temperature.config(text=str(weather["temperature"]) + "°C")
    

root.geometry = ('300x255') #Размеры для самого окна
#root.title('Прогноз погоды')
root.resizable(width=True, height=True)
root.bind("<Button-3>", WeatherReload)

#Объект Canvas необходим, чтобы на форме окна мы могли рисовать различные объекты
canvas = Canvas(root, height=300, width=255)
canvas.pack(fill=BOTH, expand = 1)

'''f_top = Frame(root, bg = 'red')
f_top.pack()'''

description = Label(canvas, width=25, height=2, 
           bg='darkorange')
temperature = Label(canvas, height=2, 
           bg='aliceblue', font=("Impact", 60))
l4 = Label(canvas, width=25, height=2, 
           bg='orange')


description.pack(side=TOP, fill=X)
temperature.pack(fill=BOTH, expand=1)

l4.pack(side=BOTTOM, fill=X, anchor=S)

WeatherReload()

root.mainloop()

