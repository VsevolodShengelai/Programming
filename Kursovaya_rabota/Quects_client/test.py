from tkinter import *
from tkinter import ttk

def addtext():
    pass

root = Tk()

wrapper1 = LabelFrame(root)
wrapper2 = LabelFrame(root)

mycanvas = Canvas(wrapper1)
mycanvas.pack(side=LEFT, fill="both", expand=1)

yscrollbar= ttk.Scrollbar(wrapper1, orient="vertical", command=mycanvas.yview)
yscrollbar.pack(side=RIGHT, fill="y")

mycanvas.configure(yscrollcommand=yscrollbar.set)

mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion=mycanvas.bbox('all')))

myframe = Frame(mycanvas)
mycanvas.create_window((0,0), window=myframe, anchor='nw')

w2But=Button(wrapper2, text='AddTExt', command=addtext)
w2But.pack()

wrapper1.pack(fill="both", expand="yes", padx=10, pady=10)
wrapper2.pack(fill="both", expand="yes", padx=10, pady=10)


for i in range(50):
    Button(myframe, text="Глава - "+str(i)).pack(pady=2) 
