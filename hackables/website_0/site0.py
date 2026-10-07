from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('home.html')

@app.route("/blog")
def my_blog():
    entries = [
        {
            'title': 'Spooky season is upon us!',
            'date': '10/29/2019',
            'content': 'Boo! Bet I scared you, huh? Halloween is my favorite holiday, it is so much fun giving out candy to other people and wearing cool costumes! What is your favorite holiday, dear reader?'
        },
        {
            'title': 'At the Zoo',
            'date': '9/27/2015',
            'content': "Hey guys. It's been a while since I last posted. I went to the Zoo today, and it was a great time. I saw a lemur, which by the way is my favorite animal! You all should check it out sometime."
        },
        {
            'title': 'My first website!',
            'date': '6/6/2014',
            'content': 'Hey guys! This is my first website! Can you believe it?! I am only 12 years old and I was able to make a website all by myself! I hope you guys enjoy. Please do not hack me :)'
        }
    ]
    return render_template('blog.html', entries=entries)

@app.route("/admin", methods=["GET", "POST"])
def admin_page():
    if request.method == "POST":
        password = request.form.get('pwd')
        if password == 'lemur2002':
            return render_template('flag.html')
        else:
            return render_template('denied.html')
    return render_template('admin.html')