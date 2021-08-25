from inspect import CO_VARKEYWORDS
from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField, StringField
from wtforms import validators
from wtforms.validators import Required, Length
class DrinkForm(FlaskForm):
    coke = RadioField('coke', choices =[('none','None'),('small','Small'),('large','Large')])
    sprite = RadioField('sprite', choices =[('none','None'),('small','Small'),('large','Large')])
    lime = RadioField('lime', choices =[('none','None'),('small','Small'),('large','Large')])
    submit = SubmitField('Submit')
class DrinkSelection(FlaskForm):
    syrup1current = "coke"
    syrup2current = "sprite"
    syrup3current = "soda water"
    syrup1 = StringField(f'First Pump (currently: {syrup1current})', [validators.required(), validators.length(max=15)])
    syrup2 = StringField(f'Second Pump (currently: {syrup2current})', [validators.required(), validators.length(max=15)])
    syrup3 = StringField(f'Third Pump (currently: {syrup3current})', [validators.required(), validators.length(max=15)])
    submit = SubmitField('Submit')
