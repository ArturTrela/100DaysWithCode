from flask import Flask

app = Flask(__name__)
app.debug = True

@app.route('/')
def hello_world():
    return 'hello_world'

def make_bold(return_z_funkcji_nadrzednej):
    def wrapper():
        return "<b>" + return_z_funkcji_nadrzednej() + "</b>"
    return wrapper

def make_underlined(return_z_funkcji_nadrzednej):
    def wrapper():
        return "<u>" + return_z_funkcji_nadrzednej() + "</u>"
    return wrapper

def make_emphasis(return_z_funkcji_nadrzednej):
    def wrapper():
        return "<em>" + return_z_funkcji_nadrzednej() + "</em>"
    return wrapper

@app.route('/bye')
@make_bold
@make_underlined
@make_emphasis
def bye():
    return 'Bye-Bye - działa'

@app.route('/<name>/<int:number>')
def greet(name, number):
    return f'Hello {name} and you are {number} years old!!'

if __name__ =='__main__':
    app.run()