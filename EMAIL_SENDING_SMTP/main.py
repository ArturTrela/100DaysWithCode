import smtplib
import datetime as dt
import random
from_google_pass = "apje xplv jdhg urkv"
my_email = "arturtrela.automation@gmail.com"
address_email = "trela.artur@gmail.com"
quotes_list=[]
now = dt.datetime.now()
day = now.weekday()

with open ("quotes.txt","r") as file:
    quotes_list = file.readlines()

quote_to_send = random.choice(quotes_list)

print(quotes_list)
def send_email():
    with smtplib.SMTP("smtp.gmail.com")as connection:
        connection.starttls()
        connection.login(user=my_email,password= from_google_pass)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=address_email,
            msg=f"Subject:Stay motivated !\n\n {quote_to_send}")


print(day)
if day == 3:
    send_email()
    print("E-mail was sended")