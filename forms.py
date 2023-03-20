from flask_wtf import FlaskForm
from wtforms import StringField, FloatField
from wtforms.validators import DataRequired, InputRequired


class CurrencyForm(FlaskForm):
    fromcurr = StringField("From Currency", validators=[
        DataRequired(), InputRequired()])
    tocurr = StringField("To Currency", validators=[
        DataRequired(), InputRequired()])
    amount = FloatField("Amount", validators=[
                        DataRequired(), InputRequired()])
