import smtplib

#SMTP : Simple Mail Transfer Protocol

myemail = "testsmtpcode11@gmail.com"
password = "#### #### #### ####" # paste your gmail>google> app password 
message = "hello"

# connection = smtplib.SMTP("smtp.gmail.com",587)
with smtplib.SMTP("smtp.gmail.com",587) as connection:
# creates SMTP session

    connection.starttls()   # start TLS for security
    connection.login(user=myemail,password=password)    # Authentication
    connection.sendmail(
        from_addr=myemail,
        to_addrs="subhamd2022@gift.edu.in",
        msg="Subject:Hello\n\nHappy birthday to you."
        ) #sending the mail
    #connection.quit() # terminating the session




