from flask.helpers import get_flashed_messages
from app.forms import DrinkForm, DrinkSelection
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
    form = DrinkSelection(request.form)
    if request.method == 'POST':
        flash(f'entered: {form.syrup1.data}, {form.syrup2.data}, {form.syrup3.data}')
        return str(get_flashed_messages())
    return render_template('settings.html', title='softmix.io', form=form)
