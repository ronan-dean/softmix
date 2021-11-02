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
    names = db.alpha.find_one({"name": "currentSyrups"})
    del names["_id"]
    del names["name"]
    pump0 = RadioField(f"names['pump0']", choices =[('0','0ML'),('30','30ML'),('60','60ML')])
    pump1 = RadioField(f"names['pump1']", choices =[('0','0ML'),('30','30ML'),('60','60ML')])
    pump2 = RadioField(f"names['pump2']", choices =[('0','0ML'),('30','30ML'),('60','60ML')])
    pump3 = RadioField(f"names['pump3']", choices =[('0','0ML'),('30','30ML'),('60','60ML')])
    pump4 = RadioField(f"names['pump4']", choices =[('0','0ML'),('30','30ML'),('60','60ML')])
    submit = SubmitField('Submit')
class DrinkSelection(FlaskForm):
    StringField = StringField('static field')
    #newSyrups = StringField('staic field')
    #newSyrupsLabel = Label('static field', 'base')
    submit = SubmitField('Submit')

    



##for x in range(numSyrups):

     ##   pumpForms.append(StringField(f'Pump {x} (currently: {syrupSelect})', [validators.required(), validators.length(max=15)]))