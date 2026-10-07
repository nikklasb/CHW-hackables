from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for
)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template('home.html')

@app.route("/flag", methods=["GET", "POST"])
def flag():
    if request.method == "POST":
        password = request.form.get('pwd')
        if password == "password123vine":
            return render_template('flag.html')
    return redirect(url_for('home', failed='yes'), code=302)