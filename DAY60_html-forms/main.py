from flask import Flask, render_template , request
import requests
from dotenv import load_dotenv
import smtplib
import os
MY_MAIL =""
MAIL_SENDER = ""
GOOGLE_PASS =""

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

@app.route('/contact', methods=["POST"])
def send_email():
    log= False
    if request.form['name'] and request.form['email']:
        to_mail =MY_MAIL
        my_mail = MAIL_SENDER
        goog_pas = GOOGLE_PASS
        quote_to_send =(f'{request.form["name"]} \n'
                        f', {request.form["email"]} \n'
                        f',{request.form["phone"]},\n'
                        f'{request.form["message"]}')
        with smtplib.SMTP("smtp.gmail.com")as connection:
            connection.starttls()
            connection.login(user=my_mail,password=goog_pas)
            connection.sendmail(
                from_addr=my_mail,
                to_addrs=to_mail,
                msg=f"Subject:Confirmation from website form  !\n\n {quote_to_send}")
        return log


if __name__ == "__main__":
    app.run(debug=True, port=5001)
