import random
import smtplib
from datetime import datetime
import pandas 

MY_EMAIL = "testsmtpcode11@gmail.com" #your email id
MY_PASSWORD = "#### #### #### ####" # paste your gmail>google> app password

 
# today = (datetime.now().month,datetime.now().day)
today = datetime.now()
today_tuple = (today.month,today.day)

data = pandas.read_csv('birthdays.csv')

# birthdays_dict = {
#     (birthday_month, birthday_day): data_row
# }

birthdays_dict = {(data_row["month"],data_row["day"]):data_row for (index,data_row) in data.iterrows()}


if today_tuple in birthdays_dict:
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    birthday_person = birthdays_dict[today_tuple] 
    with open(file_path) as letter_file:
        contains = letter_file.read()
        contains = contains.replace("[NAME]",birthday_person["name"])
    
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday!\n\n{contains}")    
        
        