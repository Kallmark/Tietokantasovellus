from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
  
class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
    
    login = SubmitField("Login")
    class Meta:
        csrf = False