from typing import Any
import requests
from urllib.request import urlopen
from PIL import Image

pokeapi_url = "https://pokeapi.co/api/v2/pokemon/"

def request_api(name: str):
    rqst = requests.get(pokeapi_url + name)
    return rqst.json()

def get_type_request(response: dict):
    tipo = [i['type']['name'].capitalize() for i in response]
    return tipo

def get_abilities_request(response: dict):
    habilidades = [i['ability']['name'].capitalize() for i in response]
    return habilidades

def get_weight_request(response: dict):
    peso = [response]
    return peso

def get_stats_request(response: dict):
    estadisticas = [f"{i['stat']['name'].capitalize()} = {i['base_stat']}" for i in response]
    return estadisticas

def get_sprite_pokemon_request(response: dict):

    imagen = response['sprites']['front_default']
    sprite = Image.open(urlopen(imagen))
    out = sprite.resize((500,550))
    return out.show()

def get_info_pokemon(name: str) -> Any:
    response = request_api(name)
    types = get_type_request(response['types'])
    abilities = get_abilities_request(response['abilities'])
    weight = get_weight_request(response['weight'])
    stats = get_stats_request(response['stats'])
    
    info = { 
        'Pokemon': [name.capitalize()],
        'Type' : types,
        'Abilities' : abilities,
        'Weight' : weight,
        'Stats': stats,
    }

    return info

def show_info_pokemon(pokemon: dict):
    for k, v in pokemon.items():
        print(f"\n{k}: ")
        for i in range(len(v)):
            print(" "*16+"%s" %v[i])
    print("")

pokemon = input("\nEnter a Pokemon: ").lower()

try: 
    info = get_info_pokemon(pokemon)
    show_info_pokemon(info)
    get_sprite_pokemon_request(request_api(pokemon))
except:
    print(f"\n\nPokemon: {pokemon.title()}, not registered in the Pokedex.\n")