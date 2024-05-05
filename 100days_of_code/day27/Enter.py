from tkinter import *


window = Tk()

def button_click():
    data = input.get()
    mylabel.config(text=data)

mylabel = Label(text="label from tkinter" ,font=('Arial',24,'bold'))
mylabel.pack()
input = Entry(width=15)
input.pack()
button = Button(text='Change',font=('Arial',8,'bold'), command=button_click)
button.pack()

window.mainloop()