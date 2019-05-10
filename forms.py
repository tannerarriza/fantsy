# forms.py

from wtforms import Form, StringField, SelectField, validators

class Mode(Form):
    choices = [('Normal', 'Normal'),
               ('FanDuel', 'FanDuel')]
    select = SelectField('Mode:', choices=choices)
    search = StringField('')
