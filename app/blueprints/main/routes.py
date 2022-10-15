from flask import render_template, request
import requests, json
from . import bp as main
from api_test import get_poke_info 

data = "https://pokeapi.co/api/v2/pokemon/"

@main.route('/pokemon', methods=['GET'])
def get_poke_info():
    my_pokedex = ["", "", "", "", ""]
                                            #name in Jinja = name in python
    return render_template('pokemon.html.j2', pokemon = my_pokedex)


@main.route('../../../api_test.py', methods=['GET'])
def api_test():
    return pokedex