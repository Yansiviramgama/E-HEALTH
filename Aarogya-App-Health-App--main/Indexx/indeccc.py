from flask import Flask, render_template, url_for, flash, redirect
from flask import request

app = Flask(__name__, template_folder='templates')
@app.route("/")

@app.route("/index")
def index():
    return render_template("index.html.html")

if __name__ == "__main__":
    app.run(debug=True)