from flask import render_template, request
import requests
import json
from .forms import LoginForm, RegisterForm
from app import app

# known needed routes: register, login, get pokemon from api, add pokemon to local
# table, add pokemon (from local table or api?) to current_user pokedex

#must have route for index -- render_template!
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# Get Pokemon for Pokedex
@app.route('/pokemon', methods=['GET', 'POST'])
def get_pokemon():
    my_pokemon = [
        
    ]
    # pokedex.append({"name": poke['name'], "type": poke['type'], "height": poke['height'], "weight": poke['weight'], "ability": poke['ability'], "hp": poke['hp'], "attack": poke['attack'], "defense": poke['defense']})
                                            #name in Jinja = name in python
    return render_template('pokemon.html.j2', pokemon = my_pokemon)


# Review Kevin's API test and Ergast to follow logic of which folders to use & ht set up

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        # LOGIN THE USER HERE
        email = form.email.data.lower()
        password = form.password.data

        if email in app.config.get('REGISTERED_USERS') and \
            password == app.config.get('REGISTERED_USERS').get(email).get('password'):
            #Login Success!!!
            return f"Login Success Welcome { app.config.get('REGISTERED_USERS').get(email).get('name') }"
        error_string = "Incorrect Email/Password Combo"
        return render_template('login.html.j2', loginerror=error_string, form=form)
    return render_template('login.html.j2', form=form)

@app.route('/register', methods=["GET","POST"])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate_on_submit():
        return "Welcome to Pokemon Battle!... Thanks for registering."
    return render_template('register.html.j2', form=form)