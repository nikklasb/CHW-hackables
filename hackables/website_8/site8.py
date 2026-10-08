from flask import (
    Flask,
    render_template,
    request,
    Response,
    redirect,
    url_for
)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template('home.html')

@app.route("/source_code")
def source():
    file_contents = open("./site8.py").read()
    return Response(file_contents, mimetype='text/plain')

@app.route("/flag", methods=["GET", "POST"])
def flag():
    # correct password stored in a file, so showing you this is not risky!
    correct_password = open('./static/password.txt', 'r').read().strip()
    if request.method == "POST":
        password = request.form.get('pwd')
        if password == correct_password:
            return render_template('flag.html')
    return redirect(url_for('home', failed='yes'), code=302)