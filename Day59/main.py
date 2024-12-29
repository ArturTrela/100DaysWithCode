from flask import Flask, render_template


app = Flask(__name__)
app.debug =True

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/')
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()



