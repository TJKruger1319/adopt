from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, Optional, URL, NumberRange, ValidationError

def validate_species(form, field):
    if field.data not in ['cat', 'dog', 'porcupine']:
        raise ValidationError("Invalid Species")  

class AddPetForm(FlaskForm):
    name = StringField("Name",  validators=[
                       InputRequired(message="Pet Name can't be blank")])
    species = StringField("Species",  validators=[
                       InputRequired(message="Species can't be blank"), validate_species])
    photo_url = StringField("Photo URL", validators=[Optional(), URL(message="Must be a URL")])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30, message="Invalid Age")])
    notes = StringField("Notes", validators=[Optional()])


class EditPetForm(FlaskForm):
    photo_url = StringField("Photo URL", validators=[Optional(), URL(message="Must be a URL")])
    notes = StringField("Notes", validators=[Optional()])
    avaliable = BooleanField("Avaliable")