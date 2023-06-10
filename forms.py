from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, Optional

class AddPetForm(FlaskForm):
    name = StringField("Name",  validators=[
                       InputRequired(message="Pet Name can't be blank")])
    species = StringField("Species",  validators=[
                       InputRequired(message="Species can't be blank")])
    photo_url = StringField("Photo URL")
    age = IntegerField("Age")
    notes = StringField("Notes")
