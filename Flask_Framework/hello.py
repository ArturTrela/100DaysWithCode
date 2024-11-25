from flask import Flask

app = Flask(__name__)
app.debug = True

@app.route('/')
def hello_world():
    return 'hello_world'

@app.route('/bye')
def bye():
    return 'Bye-Bye - działa'

@app.route('/<name>/<int:number>')
def greet(name, number):
    return f'Hello {name} and you are {number} years old!!'

if __name__ =='__main__':
    app.run()