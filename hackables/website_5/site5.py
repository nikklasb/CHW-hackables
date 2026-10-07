from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for
)
import random

app = Flask(__name__)

WORDS = [word.strip() for word in open('./basic_english_850.txt', 'r').read().split('\n')]
MESSAGES = ["nope!", "try again!", "hahaha!!!!", "man does this ever get old to you?", "mmmmm nope >:)", "so close yet so far", "swing and a miss!", "*clears throat*, yeah no."]
def random_text(collection):
    random.choice()

buttons = [
    {'text': random.choice(WORDS), 'message': random.choice(MESSAGES)} for _ in range(45)
] + [{'text': random.choice(WORDS), 'message': 'unlock password'}] + [
    {'text': random.choice(WORDS), 'message': random.choice(MESSAGES)} for _ in range(95)
]


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template('home.html', entries=buttons)

@app.route("/flag", methods=["GET", "POST"])
def flag():
    if request.method == "POST":
        password = request.form.get('pwd')
        if password == "gooddaysir2012":
            return render_template('flag.html')
    return render_template('denied.html')