from poke_api import *

pokemon = input("\nEnter a Pokemon: ").lower()
print("")

try: 
    info = get_info_pokemon(pokemon)
    show_info_pokemon(info, pokemon)

except :
    print(f"Pokemon: {pokemon.title()}, not registered in the Pokedex.\n")