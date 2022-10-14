from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import Email, DataRequired, EqualTo, ValidationError
from app import app

# Forms needed: Registration (validate!), Login, (Get Pokemon?)

class RegisterForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    email = EmailField("Email Address", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('password', message="Passwords must Match")])
    submit = SubmitField('Register')

    def validate_email(form, field):
        print(field.data)
        print(app.config.get("REGISTERED_USERS"))
        if field.data.lower() in app.config.get("REGISTERED_USERS"):
            raise ValidationError("That Email Already in Use")

class LoginForm(FlaskForm):
    email=EmailField('Email Address', validators=[DataRequired(), Email()])
    password=PasswordField('Password', validators=[DataRequired()])
    submit=SubmitField('Login')


