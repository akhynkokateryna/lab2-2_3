"app_flask.py"

from flask import Flask, render_template, request
import web_navigator

app = Flask(__name__)

@app.route('/')
def map():
    return render_template("index.html")

@app.route("/redirecting", methods = ["POST"])
def redirecting():
    if request.method == "POST":
        data = request.form
        nickname = data["name"]
        web_navigator.main(nickname)
        return render_template('new_map.html')
