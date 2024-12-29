from flask import Flask, render_template
import requests

app = Flask(__name__)
app.debug =True
api_endpoint = 'https://api.npoint.io/4c5f52246a8e640796fe'

@app.route('/post/<id>')
def post_view(id):
    response = requests.get(api_endpoint)
    posty = response.json()
    post_data =[post for post in posty if post['id'] == int(id)]
    print(f'post data to {post_data}')
    return render_template('post.html', post_data=post_data)

@app.route('/contact')
def contact():

    return render_template("contact.html" )

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/')
def home():
    response = requests.get(api_endpoint)
    posty = response.json()
    print(posty)
    return render_template("index.html", posty=posty)

if __name__ == "__main__":
    app.run()



