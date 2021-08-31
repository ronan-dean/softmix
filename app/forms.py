from inspect import CO_VARKEYWORDS
from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField, StringField, Label
from wtforms import validators
from wtforms.validators import Required, Length
from flask_pymongo import PyMongo
from app import app
record = {'field1': 'label1', 'field2': 'label2'}
app.config["MONGO_URI"] = "mongodb://localhost:27017/softmix"
mongo = PyMongo(app)
db = mongo.db
pumpForms = []
class DrinkForm(FlaskForm):
    coke = RadioField('coke', choices =[('none','None'),('small','Small'),('large','Large')])
    sprite = RadioField('sprite', choices =[('none','None'),('small','Small'),('large','Large')])
    lime = RadioField('lime', choices =[('none','None'),('small','Small'),('large','Large')])
    submit = SubmitField('Submit')
class DrinkSelection(FlaskForm):
    #newSyrups = StringField('staic field')
    #newSyrupsLabel = Label('static field', 'base')
    submit = SubmitField('Submit')

    



##for x in range(numSyrups):

     ##   pumpForms.append(StringField(f'Pump {x} (currently: {syrupSelect})', [validators.required(), validators.length(max=15)]))