from tkinter import *

window = Tk()


my_label = Label(text="I am a Label" , font=("Arial",24,"bold"))

my_label.pack()

# my_label["text"] = "New Text"
# my_label.config(text="New Year")
counter = 0

def button_clicked():
    global counter
    counter += 1
    my_label.config(text="hello" + str(counter))

def button_clicked2():
    global counter
    counter -= 1
    my_label.config(text="hello" + str(counter))

    
button = Button(text="increase me" , command=button_clicked)
button.pack()

button2 = Button(text="decrease me" , command=button_clicked2)
button2.pack()

window.mainloop()