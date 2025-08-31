from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import  PasswordField, SubmitField, EmailField, validators
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap5


app = Flask(__name__)
app.secret_key = "nalesnik"
bootstrap = Bootstrap5(app)

class LoginForm(FlaskForm):
    email = EmailField(label='email', validators=[DataRequired(),Length(min=6, max=120),Email()])
    password = PasswordField(label='password', validators=[DataRequired(),Length(min=8)])
    submit = SubmitField(label = 'Log in')



@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form =LoginForm()
    if request.method == "POST":
        if login_form.validate_on_submit():
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template('login.html',form =login_form )


@app.route("/")
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
