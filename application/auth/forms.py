from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, validators, DecimalField

#kirjautuminen 
class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
    
    login = SubmitField("Login")

    class Meta:
        csrf = False

#rekisteröinti
class RegisterForm(FlaskForm):
    name = StringField("Name", [validators.Length(max=144), validators.InputRequired()])
    username = StringField("Username", [validators.Length(max=144), validators.Length(min=5), validators.InputRequired()])
    password = PasswordField("Password", [
        validators.InputRequired(),
        validators.EqualTo('confirm', message='Passwords must match'),
        validators.Length(max=144),
        validators.Length(min=5)
        ])
    confirm = PasswordField("Repeat password", [validators.Length(max=144), validators.InputRequired()])
    register = SubmitField("Register")

    class Meta:
        csrf = False


#käyttäjätietojen ja salasanan muokkaaminen
class EditForm(FlaskForm):
    name = StringField("Name", [validators.Length(max=144), validators.InputRequired()])
    username = StringField("Username", [validators.Length(max=144), validators.Length(min=5), validators.InputRequired()])
    old_password = PasswordField("Old password", [validators.Length(max=144), validators.InputRequired()])
    new_password = PasswordField("New password", [
        validators.InputRequired(),
        validators.EqualTo('confirm', message='Passwords must match'),
        validators.Length(max=144),
        validators.Length(min=5)
        ])
    confirm = PasswordField("Repeat new password", [validators.Length(max=144), validators.InputRequired()])
    name = StringField("Name", [validators.Length(max=144), validators.InputRequired()])
    edit = SubmitField("Edit")

    class Meta:
        csrf = False

#käyttäjän tietojen muommaakimen adminin toimesta
class Edit_UserForm(FlaskForm):
    balance = DecimalField("User's balance", [validators.DataRequired(message = "Balance must be a decimal number!")])
    save = SubmitField("save")

    class Meta:
        csrf = False