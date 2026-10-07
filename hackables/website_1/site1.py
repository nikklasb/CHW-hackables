from flask import (
    Flask,
    render_template,
    request,
    Response
)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('home.html')

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
        },
        {
            'title': 'Psssst!',
            'filename': 'robot_guy.jpg',
            'description': 'Hey I\'m not actually a robot... I just want to be on their good side when they eventually take over. Take a look here and maybe you can find my secret page only for humans: https://www.robotstxt.org/robotstxt.html.'
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