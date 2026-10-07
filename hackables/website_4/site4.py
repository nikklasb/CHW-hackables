from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('home.html')

@app.route("/blog")
def my_blog():
    entries = [
        {
            'title': 'Got hacked today...',
            'date': '{d.month}/{d.day}/{d.year}'.format(d=datetime.datetime.now()),#datetime.datetime.now().strftime("%-m/%d/%Y"),
            'content': 'Somebody hacked my first blog site today... maybe I should start thinking about cybersecurity.'
        },
        {
            'title': 'Spring Spring Spring...',
            'date': '3/23/2023',
            'content': "Gosh why is it so hot today? It's not even summer yet. I think I'll stay inside and work on my websites. Can't think of a better way to spend my time."
        },
        {
            'title': 'New Years!',
            'date': '1/1/2023',
            'content': 'Happy New Years! You guys have any resolutions? My resolution is to improve my website building skills. I mean it is pretty hard when you are already a prodigy and all, but there are probably some small improvements I can make.'
        },
        {
            'title': 'Happy Almost Thanksgiving!',
            'date': '11/24/2022',
            'content': 'Hey guys, quick post to wish you all a nice Thanksgiving. I love Turkeys! Although they aren\'t a cool as Lemurs, they are way more delicious! Wishing you all lots of cranberry sauce and stuffing!'
        },
        {
            'title': 'Great burger today.',
            'date': '7/9/2022',
            'content': 'Hey guys! My parents took me to Inside-Out-Burger today. It was pretty great! Tons of different well-documented options, and the fries were delicious! Not dry at all! Though it was on the more expensive side...'
        },
        {
            'title': 'First post 👋',
            'date': '6/30/2022',
            'content': 'Hey guys. I am back after a pretty long hiatus! Did you miss me? I\'ve been busy with Nevolicty this whole time. Lots and lots of reviews... It\'s nice to be able to speak about more light hearted things sometimes.'
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