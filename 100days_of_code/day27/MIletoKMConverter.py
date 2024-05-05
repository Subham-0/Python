from tkinter import *
window = Tk()
window.title("Miles to kilometer Converter")
window.config(padx=20,pady=20)

def calculate():
    miles =float(input.get())
    km = (miles*1.60934)
    label3.config(text=km)
    
    

input = Entry(width=10,font=('Arial',15,'bold'))
input.grid(column=1,row=0)

label1 = Label(text='Miles',font=('Arial',15,'bold'))
label1.grid(column=2,row=0)
label2 = Label(text='is equal',font=('Arial',15,'bold'))
label2.grid(column=0,row=1)
label3 = Label(text='0',font=('Arial',15,'bold'))
label3.grid(column=1,row=1)
label4 = Label(text='Km',font=('Arial',15,'bold'))
label4.grid(column=2,row=1)


button = Button(text='Calculate',font=('Arial',15,'bold'),command=calculate)
button.grid(column=1,row=2)

window.mainloop()

