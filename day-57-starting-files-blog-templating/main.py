from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/post/<id>')
def show_post(id):
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    posts = requests.get(blog_url).json()
    new = [_ for _ in posts if _['id'] == int(id)]
    print(type(new))
    return render_template('post.html',new = new)


@app.route('/')
def home():
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    posts = requests.get(blog_url).json()
    return render_template("index.html", posts=posts)

if __name__ == "__main__":
    app.run(debug=True)
