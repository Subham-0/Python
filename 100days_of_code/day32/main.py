import random
import smtplib
import datetime as dt 

MY_EMAIL = "testsmtpcode11@gmail.com"
MY_PASSWORD =  "#### #### #### ####" # paste your gmail>google> app password

 
now = dt.datetime.now()
weekday = now.weekday()

if weekday == 4:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    
    print(quote)
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs="dashsubham2002@gmail.com",
                                msg=f"Subject:Monday Motivation\n\n{quote}")