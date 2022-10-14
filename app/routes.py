from flask import render_template, request
import requests
from .forms import LoginForm, RegisterForm
from app import app

#must have route for render template!
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/pokemon', methods=['GET'])
def pokemon():
    my_pokemon = [
        
    ]
                                            #name in Jinja = name in python
    return render_template('pokemon.html.j2', pokemon = my_pokemon)


@app.route('/api_test', methods=['GET'])
def api_test():
    return {"":"Smart dude",
            "":"Smelly Dude", 
            "": "Chill Dude", 
            "" : "Pokemon Dude", 
            "": "Fun Dude",
            "": "Joke destroyer!"}

# @app.route('/ergast', methods=['GET', 'POST'])
# def ergast():
#     if request.method =='POST':
#         year = request.form.get("year")
#         r = request.form.get("round")
#         url = f'http://ergast.com/api/f1/{year}/{r}/driverStandings.json'
#         response = requests.get(url)
#         if not response.ok:
#             error_string = "We had an Unexpected Error"
#             return render_template('ergast.html.j2', error = error_string)
#         if not response.json()["MRData"]["StandingsTable"]["StandingsLists"]:
#             error_string = "You have a Bad Year / Round Combo/  Please Try Again"
#             return render_template('ergast.html.j2', error = error_string)
#         data = response.json()["MRData"]["StandingsTable"]["StandingsLists"][0]['DriverStandings']
#         new_data=[]
#         for racer in data:
#             racer_dict={
#                 "last_name":racer['Driver']['familyName'],
#                 "first_name":racer['Driver']['givenName'],
#                 "position":racer['position'],
#                 "wins":racer['wins'],
#                 "DOB":racer['Driver']['dateOfBirth'],
#                 "nationality":racer['Driver']['nationality'],
#                 "constructor":racer['Constructors'][0]['name']
#             }
#             new_data.append(racer_dict)
#         return render_template('ergast.html.j2', racers=new_data)

#     return render_template('ergast.html.j2')

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