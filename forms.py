from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired, Length


class CreateDeviceForm(FlaskForm):
    deveui = StringField('devEUI', validators=[InputRequired(), Length(min=7, max=255)])
    board = StringField('Board Name', validators=[InputRequired(), Length(min=5, max=255)])
