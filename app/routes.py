from flask.helpers import get_flashed_messages
from app.forms import DrinkForm
from flask import render_template, request, flash
from flask_bs4 import Bootstrap
from app import app 
import os
Bootstrap(app)
@app.route('/')
@app.route('/index', methods=['GET', 'POST'])

def index():
    form = DrinkForm(request.form)
    if request.method == 'POST':
        flash('Coke: {} Sprite {} Soda Water {}'.format(form.coke.data, form.sprite.data, form.lime.data))
        return str(get_flashed_messages())

    drinks = ["Coke", "Sprite", "Soda Water"]
    return render_template('form.html', title='Softmix.io', drinks=drinks, form=form)
@app.route('/settings/', methods=['GET', 'POST'])
def settings():
    drinks = ["Coke", "Sprite", "Soda Water"]
    return render_template('index.html', title='softmix.io', drinks=drinks)
