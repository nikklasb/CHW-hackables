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

@app.route("/offers")
def offers():
    user = request.args.get('user')
    items = [
        {
            'name': 'Toaster',
            'price': 99.99,
            'description': 'Quality toaster, minimal damage. 4 bread slots and removable crum tray.'
        },
        {
            'name': 'HP Laptop',
            'price': 249.99,
            'description': 'HP Omnibook used for only 2 years. Completely refurbished and upgraded with 16gb additional RAM.'
        },
        {
            'name': 'XBox 360',
            'price': 157.00,
            'description': 'Used, partially damaged. Two additional controllers and copies of Bioshock and Halo 3.'
        },
        {
            'name': 'HP Laser Printer',
            'price': 899.99,
            'description': 'Almost completely new Laser Jet Printer. Includes power cord, additional tray. Paper and ink is not included.'
        }
    ]
    if (user == 'super'):
        for item in items:
            item['price'] = item['price'] * 0.8
        items.append({
            'name': 'flag',
            'price': 0,
            'description': 'url_p4r4m373r5_4r3_n07_54f3_317h3r'
        })
    for item in items:
        item['price'] = f"${item['price']:,.2f}"
    return render_template('offers.html', items=items)

@app.route("/super-secret-page")
def solution():
    return render_template('flag.html')