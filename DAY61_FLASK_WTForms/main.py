from django.forms import EmailField
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField


app = Flask(__name__)

app.secret_key = "nalesnik"

class MyForm(FlaskForm):
    email = StringField('email')
    password = StringField('password')

@app.route('/login')
def login():
    form =MyForm()

    return render_template('login.html', form = form )


@app.route("/")
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
