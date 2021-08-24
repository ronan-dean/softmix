from app.forms import DrinkForm
from flask import render_template, request
from flask_bs4 import Bootstrap
from app import app 
import os
Bootstrap(app)
@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = DrinkForm(request.form)
    if request.method == 'POST':
        return 'OH YEA'
    drinks = ["Coke", "Sprite", "Soda Water"]
    return render_template('form.html', title='Softmix.io', drinks=drinks, form=form)
