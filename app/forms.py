from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField, RadioField
from wtforms.validators import Email, DataRequired, EqualTo, ValidationError
from app.models import User
from jinja2.utils import markupsafe
from app import app

# Forms needed: Registration (avatar, validate!), Login, Edit, (Get Pokemon?), 
# Minor edits to what we did in class for login, register, edit
# Avatar (not random) pokeball from: https://www.flaticon.com/free-icons/pokemon
# Favicon: https://www.flaticon.com/free-icon/pokeball_287221

class LoginForm(FlaskForm):
    email=EmailField('Email Address', validators=[DataRequired(), Email()])
    password=PasswordField('Password', validators=[DataRequired()])
    submit=SubmitField('Login')

class RegisterForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    email = EmailField("Email Address", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), 
        EqualTo('password', message="Passwords Must Match")])
    submit = SubmitField('Register')

    a1_img = markupsafe.Markup(f'<img src="https://www.flaticon.com/free-icon/gaming_1752776" height="75px">')
    a2_img = markupsafe.Markup(f'<img src="https://www.flaticon.com/free-icon/gaming_1752731" height="75px">')
    a3_img = markupsafe.Markup(f'<img src="https://www.flaticon.com/free-icon/gaming_1752699" height="75px">')
    a4_img = markupsafe.Markup(f'<img src="https://www.flaticon.com/free-icon/gaming_1752763" height="75px">')
    a5_img = markupsafe.Markup(f'<img src="https://www.flaticon.com/free-icon/gaming_1752871" height="75px">')

    icon = RadioField("Avatar", validators=[DataRequired()], choices = [(a1_img),(a2_img),(a3_img),(a4_img),(a5_img)])

    def validate_email(form, field):
        print(field.data)
        same_email_user = User.query.filterby(email=field.data).first()
        if same_email_user:
            raise ValidationError("That Email Already Registered")

class EditForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    email = StringField("Email Address", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('password', message="Passwords must Match")])
    submit = SubmitField('Update')

    a1_img = markupsafe.Markup(f'<img src="https://www.flaticon.com/free-icon/gaming_1752776" height="75px">')
    a2_img = markupsafe.Markup(f'<img src="https://www.flaticon.com/free-icon/gaming_1752731" height="75px">')
    a3_img = markupsafe.Markup(f'<img src="https://www.flaticon.com/free-icon/gaming_1752699" height="75px">')
    a4_img = markupsafe.Markup(f'<img src="https://www.flaticon.com/free-icon/gaming_1752763" height="75px">')
    a5_img = markupsafe.Markup(f'<img src="https://www.flaticon.com/free-icon/gaming_1752871" height="75px">')

    # because Avatars are not random, user choice is still an option - removed "Don't Change"
    icon = RadioField("Avatar", validators=[DataRequired()], choices = [(a1_img),(a2_img),(a3_img),(a4_img),(a5_img)])

