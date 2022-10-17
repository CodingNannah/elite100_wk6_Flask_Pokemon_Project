# Pulling out data for 5 different pokemon:
# Name
# at least one ability's name, 
# base_experience: for Battle Project, this becomes: hp, attack, defense
# URL for its sprite ex.'front_shiny'

import requests, json

data = "https://pokeapi.co/api/v2/pokemon/"

def get_poke_info(data, poke_m):
    new_data = []
    pokedex = {}
    print(data)
    
    pokemon = f'{data}{poke_m}'
    print(pokemon.lower())
    
    response = requests.get(pokemon.lower())
    print(response)
    
    response.json()    
       
    poke_name = f"{response.json()['forms'][0]['name'].title()}"
       
    pokedex[poke_name] = {
        'name':response.json()['name'],
        'type':response.json()['types'][0]['type']['name'],
        'height':response.json()['height'],
        'weight':response.json()['weight'],
        'ability':response.json()['abilities'][0]['ability']['name'],
        # 'ability2':response.json()['abilities'][1]['ability']['name'],
        # 'base_experience':response.json()['base_experience'],
        'hp':response.json()['stats'][0]['base_stat'],
        'attack':response.json()['stats'][1]['base_stat'],
        'defense':response.json()['stats'][2]['base_stat'],
        'sprite':response.json()['sprites']['versions']['generation-v']['black-white']['animated']['front_shiny']
        }

    # return pokedex
    # print(pokedex)
    # new_data.append(pokedex)
    # return new_data
    
get_poke_info(data, "Tentacruel")
get_poke_info(data, "Charmander") 
get_poke_info(data, "Yanmega")
get_poke_info(data, "Serperior")
get_poke_info(data, "Articuno")
get_poke_info(data, "Raichu") # what Pikachu turns into!
get_poke_info(data, "Meowth")
get_poke_info(data, "Lugia")
get_poke_info(data, "Psyduck")
get_poke_info(data, "Vanilluxe")
get_poke_info(data, "Mewtwo")
get_poke_info(data, "Scizor")
get_poke_info(data, "Charizard")
get_poke_info(data, "Lucario")
get_poke_info(data, "Ninetales")
get_poke_info(data, "Raticate")
get_poke_info(data, "Jolteon")
get_poke_info(data, "Machamp")
get_poke_info(data, "Tyranitar")
get_poke_info(data, "Rhydon")
get_poke_info(data, "Venomoth")
get_poke_info(data, "Venusaur")
get_poke_info(data, "Houndoom")
get_poke_info(data, "Magneton")
get_poke_info(data, "Escavalier")

# These do not have a 2nd ability:

get_poke_info(data, "Xerneas")
get_poke_info(data, "Zoroark")
get_poke_info(data, "Celebi")
get_poke_info(data, "Archeops")
get_poke_info(data, "Zekrom")