
from tkinter import *
from tkinter import messagebox
from random import choice , randint , shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4)
    )]

    password_list =password_letter+password_symbols+password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0,END)
    password_entry.insert(0,password)
    pyperclip.copy(password)
   



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=website_entry.get()
    email=email_entry.get()
    password = password_entry.get()
    if website=="" or password=="":   
        messagebox.showerror(message="the wesite and password file must required")
    else:
        is_ok = messagebox.askokcancel(title=website,message=f"These are the details entered: \nEmail:{email}\nPassword:{password}\n Is it ok to Save?")
        if is_ok:
            with open("data.txt","a") as data_file:
                data_file.write(f"{website} || {email} || {password}\n")
                website_entry.delete(0,END)
                password_entry.delete(0,END)



  


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")

window.config(padx=50,pady=50)

locker_image = PhotoImage(file="logo.png")
canvas = Canvas(width=200,height=200)
canvas.create_image(100,100,image=locker_image)
canvas.grid(column=1,row=0)


website_lable = Label(text='Website')
website_lable.grid(column=0,row=1)
email_lable = Label(text='Email/Username')
email_lable.grid(row=2,column=0)
password_lable = Label(text='Password')
password_lable.grid(row=3,column=0)

website_entry = Entry(width=55)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()
email_entry = Entry(width=55)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"dashsubham2002@gmail.com")
password_entry = Entry(width=37)
password_entry.grid(row=3,column=1,sticky="e")

password_button = Button(text='Generate Password',command=generate_password)
password_button.grid(row=3,column=2)

add_button = Button(text='Add',width=47,command=save)
add_button.grid(row=4,column=1,columnspan=2)
window.mainloop()