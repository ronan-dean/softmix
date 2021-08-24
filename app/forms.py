from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField
from wtforms.validators import Required
class DrinkForm(FlaskForm):
    coke = RadioField('coke', choices =[('none','None'),('small','Small'),('large','Large')])
    sprite = RadioField('sprite', choices =[('none','None'),('small','Small'),('large','Large')])
    lime = RadioField('lime', choices =[('none','None'),('small','Small'),('large','Large')])
    submit = SubmitField('Submit')