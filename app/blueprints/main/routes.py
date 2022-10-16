from flask import render_template, request
import requests, json
from . import bp as main
from api_test import get_poke_info 

# use ergast from class as models

data = "https://pokeapi.co/api/v2/pokemon/"

@main.route('/pokemon', methods=['GET'])
def pokemon():
    my_pokedex = ["", "", "", "", ""]
                                            #name in Jinja = name in python
    return render_template('pokemon.html.j2', pokemon = my_pokedex)


@main.route('../../../api_test', methods=['GET'])
def api_test():
    return { }


@main.route('/pokemon', methods=['GET', 'POST'])
def pokemon():
    if request.method =='POST':
        name = request.form.get("name")
        url = f'https://pokeapi.co/api/v2/pokemon/{name}'
        response = requests.get(url)
        if not response.ok:
            error_string = "Unexpected Error"
            return render_template('pokemon.html.j2', error = error_string)
        if not response.json()['name']:
            error_string = "Either you misspelled that name, or that Pokemon is too tired to join you today. Please Try Again"
            return render_template('pokemon.html.j2', error = error_string)
        data = response.json()["name"]
        new_data=[]
        for pokemon in data:
            my_pokedex = {
            'name':pokemon['name'],
            'type':pokemon['types'][0]['type']['name'],
            'height':pokemon['height'],
            'weight':pokemon['weight'],
            'ability':pokemon['abilities'][0]['ability']['name'],
            # 'ability2':pokemon['abilities'][1]['ability']['name'],
            # 'base_experience':pokemon['base_experience'],
            'hp':pokemon['stats'][0]['base_stat'],
            'attack':pokemon['stats'][1]['base_stat'],
            'defense':pokemon['stats'][2]['base_stat'],
            'sprite':pokemon['sprites']['versions']['generation-v']['black-white']['animated']['front_shiny'],
            }
            new_data.append(my_pokedex)
        return render_template('pokemon.html.j2', pokemon = new_data)

    return render_template('pokemon.html.j2')