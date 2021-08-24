from flask import render_template
from app import app 
@app.route('/')
@app.route('/index')
def index():
    drinks = ["Coke", "Sprite", "Soda Water"]
    return render_template('index.html', title='Softmix.io', drinks=drinks)
