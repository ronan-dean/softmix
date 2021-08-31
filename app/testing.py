from app.forms import DrinkSelection
from wtforms.fields.core import StringField


syrup = []

result = {
    'name': 'currentSyrups',
    '_id': 'bigbrain',
    'pump0': 'sprite',
    'pump1': 'coke',
    'pump2': 'soda',
}
class form:
    pumpForms = []
    del result['name']
    del result['_id']
    for key, value in result.items():
        setattr(DrinkSelection, key, StringField(value))
    print(result)
    
form()

