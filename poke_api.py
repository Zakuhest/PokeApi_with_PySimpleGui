from poke_data import *
import requests
import PySimpleGUI as sg

pokeapi_url = "https://pokeapi.co/api/v2/pokemon/"

def request_api(name: str):
    rqst = requests.get(pokeapi_url + name)
    return rqst.json()

def get_sprite_pokemon_request(response: dict):
    # imagen = response['sprites']['other']['home']['front_default']
    imagen = response['sprites']['front_default']
    return imagen

def get_info_pokemon(name: str) -> dict:
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

def show_info_pokemon(pokemon: dict, name: str):
    url = get_sprite_pokemon_request(request_api(name))
    response = requests.get(url, stream=True)

    sg.theme('Dark')
    col_info1, col_info2 = [], []

    for k, v in pokemon.items():
        if k == 'Stats':
            col_info2.append([sg.Text(f"\n{k}: ")])
            for i in range(len(v)):
                col_info2.append([sg.Text(" "*16+"%s" %v[i])])
                col_info2.append([sg.Text("")])
            continue
        col_info1.append([sg.Text(f"\n{k}: ")])
        for i in range(len(v)):
            col_info1.append([sg.Text(" "*16+"%s" %v[i])])

    col_pokemon_sprite = [
        [sg.Image(size=(150,90), data = response.raw.read())]
    ]

    layout = [
        [
            sg.Column(col_info1),
            sg.VSeperator(),
            sg.Column(col_info2),
            sg.VSeperator(),
            sg.Column(col_pokemon_sprite,background_color='DarkRed')
            
        ],
        [
            sg.Button('Exit',button_color="DarkGreen",expand_x=True)
        ]
    ]
    
    window = sg.Window('Pokedex', layout)

    while True:
        event, values = window.read()  # type: ignore
        if event == 'Exit' or event == sg.WIN_CLOSED:
            break

    window.close()

