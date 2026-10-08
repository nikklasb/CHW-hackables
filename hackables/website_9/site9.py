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

@app.route("/robots.txt")
def robots():
    file_contents = open("./static/robots.txt", "r").read()
    return Response(file_contents, mimetype='text/plain')

@app.route("/xhklow/klm")
def password_hints():
    return render_template('hints.html')

@app.route("/mklmbvf2")
def password_entry():
    user = request.args.get("user", "none")
    return render_template('entry.html', value=user)

@app.route("/flag", methods=["GET", "POST"])
def solution():
    if request.method == "POST":
        user = request.form.get("usr", "none")
        password = request.form.get("pwd", "")
        if user == "anon" and password == "gettingcloser":
            return render_template('flag.html')
    file_contents = open("./static/wrong.txt", "r", encoding="utf-8").read()
    return Response(file_contents, mimetype='text/plain')