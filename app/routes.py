from flask.helpers import get_flashed_messages
from app.forms import DrinkForm, DrinkSelection, pumpForms
from flask import render_template, request, flash, redirect
from wtforms import RadioField, SubmitField, StringField, Label
from flask_bs4 import Bootstrap
from app import app 
import os
from flask_pymongo import PyMongo
from flask_wtf import FlaskForm

Bootstrap(app)
app.config["MONGO_URI"] = "mongodb://localhost:27017/softmix"
mongo = PyMongo(app)
db = mongo.db


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
    class DrinkSelection(FlaskForm):
        upSyrup = StringField('upSyrup')
        submit = SubmitField('Submit')
    form = DrinkSelection(request.form)
    if request.method == 'POST':
        result1 = db.alpha.find_one_and_update({"name": "currentSyrups"}, {"$set": {'pump0': form.syrup1.data, 'pump1': form.syrup2.data, 'pump2': form.syrup3.data}})
        result1
        flash("Your syrups have been updated!")
        return redirect(request.url)
    result = db.alpha.find_one({"name": "currentSyrups"})
    del result["_id"]
    del result["name"]
    result2 = result
    for key, value in result.items():
        setattr(DrinkSelection, key, Label('static field', str(key) + str(" currently has ") + value))
    DrinkSelection.upSyrup = StringField('upSyrup')
    for key, value in result2.items():
        setattr(DrinkSelection, key, StringField(str(key)))
    return render_template('settings.html', title='softmix.io', form=form, result=result, result2=result2)
