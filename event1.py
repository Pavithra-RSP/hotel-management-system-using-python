#from tkinter import*
import tkinter as tk
from tkinter import messagebox
from tkinter import font
#from PIL import ImageTk,Image

def home():
    parent=tk.Tk()
    parent.geometry("1500x720")
    parent.title("bank")
    label_wel=tk.Label(parent,text="event management system",font=("times new roman",30),bg="#000000",fg="#DC143C")
    label_wel.configure(bg="darkolivegreen4")
    label_wel.pack(pady=30)

    frame=tk.Frame(parent,width=500,height=250)
    frame.place(relx=0.0,rely=0.0)
    #img=ImageTk.PhotoImage(Image.open("image.jpeg"))
    #label=tk.Label(frame,image=img)
    #label.pack()
    parent.mainloop()