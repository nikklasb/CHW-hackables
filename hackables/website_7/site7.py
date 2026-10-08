from flask import (
    Flask,
    render_template,
    request,
    Response
)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/caesar")
def caesar_fan_page():
    return render_template('caesar.html')

@app.route("/flag", methods=["GET", "POST"])
def solution():
    if request.method == "POST":
        password = request.form.get("pwd")
        if password == "ettubrute":
            return render_template('flag.html')
    return render_template('denied.html')