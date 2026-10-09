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

@app.route("/robots_help")
def robots_help():
    text = open('./static/robots_explanation.txt', 'r').read()
    return Response(text, mimetype='text/plain')

@app.route("/favorites")
def favorites():
    entries = [
        {
            'title': 'The Iron Giant',
            'filename': 'iron_giant.jpg',
            'description': 'Hes so fun and very friendly.'
        },
        {
            'title': 'WALL-E',
            'filename': 'wall-e.png',
            'description': "Such a friendly robot, and cleaning up the Earth."
        },
        {
            'title': 'Baymax',
            'filename': 'baymax.webp',
            'description': 'Such a selfless robot, truly an inspiration for all of us.'
        }
    ]
    return render_template('favorites.html', entries=entries)

@app.route("/robots.txt")
def robots():
    file_contents = open("./static/robots.txt", "r").read()
    return Response(file_contents, mimetype='text/plain')

@app.route("/super-secret-page")
def solution():
    return render_template('flag.html')