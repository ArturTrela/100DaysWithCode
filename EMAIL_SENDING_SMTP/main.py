import smtplib

from_google_pass = "apje xplv jdhg urkv"
my_email = "arturtrela.automation@gmail.com"
address_email = "trela.art@gmail.com"
with smtplib.SMTP("smtp.gmail.com")as connection:
    connection.starttls()
    connection.login(user=my_email,password= from_google_pass)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=address_email,
        msg="Subject:hello !\n\n this is a body of my e-mail")
