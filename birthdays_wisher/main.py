##################### Normal Starting Project ######################


# 4. Send the letter generated in step 3 to that person's email address.
# HINT 1: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
# HINT 2: Remember to call .starttls()
# HINT 3: Remember to login to your email service with email/password. Make sure your security setting is set to allow less secure apps.
# HINT 4: The message should have the Subject: Happy Birthday then after \n\n The Message Body.

import pandas as pd
import smtplib
import datetime as dt
import random

from_google_pass = "apje xplv jdhg urkv"
my_email = "arturtrela.automation@gmail.com"
address_email = "trela.artur@gmail.com"
final_letter = []
final_mail =[]
# take a today's date
now = dt.datetime.now()
today_month = now.month
today_day = now.day
today = (today_month, today_day)


def mail_sender():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=from_google_pass)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthdays_dict[today]["email"],
            msg=f'Happy Birthday!!!\n\n{letter}'

        )
    print("Mail has been send")

# read brithdays from file
data = pd.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
pointer = random.randint(1, 3)
if today in birthdays_dict:
    with open(f"./letter_templates/letter_{pointer}.txt", "r") as file:
        letter = file.read()

    letter = letter.replace("[NAME]", birthdays_dict[today]["name"])


    with open("final_letter.txt" ,"w") as final:
        final.writelines(letter)




    mail_sender()
