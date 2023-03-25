from flask import Flask, render_template

app = Flask(__name__)

@app.route("/") # http://127.0.0.1:5000/
def home():
    return render_template("index.html")

@app.route("/about") # http://127.0.0.1:5000/about
def about():
    return render_template("about.html")

# local host http://127.0.0.1:5000 http://localhost:5000
# production host http://98.91.65.12 http://mywebsite.com
