from flask.helpers import get_flashed_messages
from app.forms import DrinkForm, DrinkSelection, pumpForms
from flask import render_template, request, flash, redirect
from wtforms import RadioField, SubmitField, StringField, Label
from flask_bs4 import Bootstrap
from app import app 
import os
from flask_pymongo import PyMongo
from flask_wtf import FlaskForm
#from app.backend.fillscript import dispense # if not connected to the ardunio this will prevent the server from starting

Bootstrap(app)
app.config["MONGO_URI"] = "mongodb://localhost:27017/softmix"
mongo = PyMongo(app)
db = mongo.db
col = db.alpha

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])

def index():
    form = DrinkForm(request.form)
    names = db.alpha.find_one({"name": "currentSyrups"})
    del names["_id"]
    del names["name"]
    if request.method == 'POST':
        flash("Dispensing your selection now: Pump0: {} Pump1: {} Pump2: {} Pump3: {} Pump4: {}".format(form.pump0.data, form.pump1.data, form.pump2.data, form.pump3.data, form.pump4.data))
        #dispense(int(form.pump0.data), 0)
        #dispense(int(form.pump1.data), 'w')
        #dispense(int(form.pump2.data), 2)
        #dispense(int(form.pump3.data), 3)
        #dispense(int(form.pump4.data), 4)
        return render_template('form.html', title='Softmix.io', drinks=names, form=form, dispensedFlag=True)
    drinks = ["Coke", "Sprite", "Soda Water"]
    return render_template('form.html', title='Softmix.io', drinks=names, form=form, dispensedFlag=False)

names =  {
    'name1': 'currentSyrups',
    'name2': 'bigbrain',
    'name3': 'sprite',
    'name4': 'coke',
    'name5': 'soda',
    'name6': 'soda',
    'name7': 'soda',
    'name8': 'soda',
}
names2 =  {
    'name1': 'currentSyrups',
    'name2': 'bigbrain',
    'name3': 'sprite',
    'name4': 'coke',
    'name5': 'soda',
}
@app.route('/settingsbeta/', methods=['GET', 'POST'])
def settingsbeta():
    class F(FlaskForm):
        methods=['GET', 'POST']
        pass
    F.username = StringField(label='username')
    names = db.alpha.find_one({"name": "currentSyrups"})
    del names["_id"]
    del names["name"]
    for key, value in names.items():
        setattr(F, key, StringField(label=value.title(), default=value))
    form = F(request.form)
    if request.method == 'POST':
        newvalues = {"$set": {"pump0": form.pump0.data, "pump1": form.pump1.data, "pump2": form.pump2.data, "pump3": form.pump3.data, "pump4": form.pump4.data} }
        col.update_one(names, newvalues)
        flash("Updated messages")
        return redirect(request.referrer)
    return render_template('settingsbeta.html', title='softmix.io', form=form, names=names, names2=names2)

