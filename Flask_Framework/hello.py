from flask import Flask

app = Flask(__name__)
app.debug = True

@app.route('/')
def hello_world():
    return 'hello_world'

@app.route('/bye')
def bye():
    return 'Bye-Bye - działa'

@app.route('/<name>')
def greet(name):
    return f'Hello {name}!'

if __name__ =='__main__':
    app.run()