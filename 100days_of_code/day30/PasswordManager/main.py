
import json
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
    
    new_data = {
        website:{
            "email":email,
            "password":password,
        }
    }
    if website=="" or password=="":   
        messagebox.showerror(message="the wesite and password file must required")
    else:
        # with open("data.json","w") as data_file:
            #how to write
            # json.dump(new_data,data_file,indent=4)
            
            #how to read
            # json_string = data_file.read()
            # data = json.loads(json_string)
            # print(data)
            
            #how to update
        try:
            with open("data.json","r") as data_file:
                #reading old data
                json_string = data_file.read()
                data = json.loads(json_string)
        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(new_data,data_file,indent=4)
        else:
            #updating old data with new data
            data.update(new_data)
            with open("data.json","w") as data_file:
                #saving updated data
                json.dump(data,data_file,indent=4)
        finally:    
            website_entry.delete(0,END)
            password_entry.delete(0,END)
# ---------------------------- FIND WEBSITE ------------------------------- #        
def search_details():
    website=website_entry.get()
    if website=="":  
        messagebox.showerror(message="Please enter the website name")
    else:
        try:
            with open("data.json","r") as data_file:
                #reading old data
                json_string = data_file.read()
                data = json.loads(json_string)
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No Data File Found.")
        else:
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website,message=f"Email: {email}\nPassword: {password}")
            else:
                messagebox.showinfo(title="Error",message=f"No details for {website} exits.")
    


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

website_entry = Entry(width=37)
website_entry.grid(row=1,column=1,sticky="e")
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

search_button = Button(text='Search',width=14,command=search_details)
search_button.grid(row=1,column=2)

window.mainloop()