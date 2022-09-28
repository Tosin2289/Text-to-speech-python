import tkinter
import pyttsx3
import sys
from tkinter import *


top = Tk()
top.title("Text to speech")
top.geometry("300x300")


e1=Entry(top,font=("arial",20,"bold"))
e1.pack(fill="both")

def speech():
    fri=pyttsx3.init()
    say=e1.get()
    fri.say(say)
    fri.runAndWait()
    
b1=Button(top,text="speech",font=("arial",20,"bold"),command=speech,bg="blue")
b1.place(x=0,y=100)

def ex():
    sys.exit()
b2=Button(top,text="exit",font=("arial",20,"bold"),command=ex,bg="red")
b2.place(x=200,y=100)

top.mainloop()