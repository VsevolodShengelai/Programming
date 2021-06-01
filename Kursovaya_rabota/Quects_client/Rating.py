from tkinter import *
import requests
import json

def init(root):

    def destroy():
        RatingFrame.destroy()

    RatingFrame = Frame(root, bg = 'SpringGreen', height = 630, width = 385)
    RatingFrame.place(x = 0, y = 0)
    Rating.pack_propagate(False)


