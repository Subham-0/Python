import tkinter

window = tkinter.Tk()
window.title('My first GUI Program')
window.maxsize(width=500,height=300)


#Lable
label = tkinter.Label(text='I am a lable',font=("Arial",24,"bold"))
label.pack(side='bottom') #expand=True

window.mainloop()