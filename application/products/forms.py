from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators, DecimalField, SubmitField

class ProductForm(FlaskForm):
    name = StringField("Product name", [validators.Length(min=2, message = "Minimum lenght for nme is 2 characters!")])
    amount = IntegerField("Products amount", [validators.NumberRange(min=0, max=9999, message = "Numbers must be between 0-9999!")])
    price = DecimalField("Products price", [validators.DataRequired(message = "Balance must be a decimal number!")])

    save = SubmitField("Save")
    class Meta:
        csrf = False