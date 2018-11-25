from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import IntegerField

class ProductForm(FlaskForm):
    name = StringField("Product name")
    amount = IntegerField("Products amount")
    price = IntegerField("Products price")
    class Meta:
        csrf = False