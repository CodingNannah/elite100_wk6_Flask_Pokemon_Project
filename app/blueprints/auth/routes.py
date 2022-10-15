from flask import render_template, request, flash, redirect, url_for
from .forms import LoginForm, RegisterForm, EditProfileForm
from . import bp as auth
from app.models import User
from flask_login import login_user, login_required, logout_user, current_user


# create auth routes for register, login, logout, edit
# @auth.routh empowers the dev it's attached to

# REGISTER
# requires methods GET and POST
@auth.route('/register', methods=["GET","POST"])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate_on_submit():
        new_user_data = {
            "first_name" : form.first_name.data.title(),
            "last_name" : form.last_name.data.title(),
            "email": form.email.data.lower(),
            "password": form.password.data,
            "icon" : form.icon.data
        }

# notice how Kevin uses new_user_data and new_user_object

        # new_user_object is equal to/is empty User()
        new_user_object = User()
        # get new user info from new user data
        new_user_object.from_dict(new_user_data)
        # save data that has changed inside a table
        # do not save this to User()
        new_user_object.save()

        # REGISTRATION Success; green:
        flash('You have successfully REGISTERED.', 'success')
        return redirect(url_for("auth.login"))

    # creation of actual registration:
    return render_template('register.html.j2', form=form)


# LOG IN
# methods for login: GET & POST 
@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data.lower()
        # do not lowercase passwords!
        password = form.password.data 
                                # colname = value # one and only one!
        u = User.query.filter_by(email=email).first() 
        if u and u.check_hashed_password(password):
            # Login Success; green:
            flash('You have successfully logged IN.', 'success')
            login_user(u)
            # may change where successful logged in user is dropped off...
            return redirect(url_for('social.index'))
       
        error_string = "Incorrect Email or Password"
        return render_template('login.html.j2', loginerror=error_string, form=form)
    
    return render_template('login.html.j2', form=form)

# LOG OUT
# logout does not require POST method
@auth.route('/logout', methods=['GET'])
# must be logged in before can be logged out
@login_required 
def logout():
    logout_user()
    # Log OUT Success; blue:
    flash('You have successfully logged OUT.', 'primary')
    # may change where successful logged in user is dropped off...
    return redirect(url_for("social.index"))


# EDIT
# edit requires GET and POST
# "profile" works
@auth.route('/edit_profile', methods=['GET','POST'])
def edit_profile():
    form = EditProfileForm()
    if request.method == 'POST' and form.validate_on_submit():
        # edit same as new_user_data
        edited_user_data = {
            "first_name" : form.first_name.data.title(),
            "last_name" : form.last_name.data.title(),
            "email": form.email.data.lower(),
            "password": form.password.data,
            "icon" : form.icon.data
        }
        # edited, because received here after user editED data
        user = User.query.filter_by(email = edited_user_data["email"]).first()
        if user and user.email != current_user.email:
            # Warning
            flash('Poke Master to edit and Current Poke Master Do Not Match! Unable to edit at this time.', 'danger')
            return redirect(url_for("auth.edit_profile"))
            
        current_user.from_dict(edited_user_data)
        current_user.save()
        # Success
        flash("Poke Master information UPDATED.", "success")
        # may drop user off elsewhere...
        return redirect(url_for("social.index"))

    return render_template('register.html.j2',form=form)

