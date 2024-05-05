from tkinter import *
window = Tk()
window.minsize(width=500,height=500)
window.config(padx=100,pady=100)

my_label = Label(text="New Text",font=('Arial',12,'bold'))
my_label.grid(column=0,row=0)
my_label.config(padx=20,pady=20)

my_button = Button(text='click here',font=('Arial',12,'bold'))
my_button.grid(column=1,row=1)

new_button = Button(text='new button',font=('Arial',12,'bold'))
new_button.grid(column=2,row=0)

entry = Entry()
entry.grid(column=3,row=2)

window.mainloop()