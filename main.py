import re
import requests
"""
Obtén cuantos pokemones poseen en sus nombres “at” y tienen 2 “a” en su nombre, incluyendo la primera del “at”.
Tu respuesta debe ser un número.
¿Con cuántas especies de pokémon puede procrear raichu? (2 Pokémon pueden procrear si están dentro del mismo egg group).
Tu respuesta debe ser un número. Recuerda eliminar los duplicados.
Entrega el máximo y mínimo peso de los pokémon de tipo fighting de primera generación (cuyo id sea menor o igual a 151).
Tu respuesta debe ser una lista con el siguiente formato: [1234, 12], en donde 1234 corresponde al máximo peso y 12 al mínimo.
"""
all_pokemons = []
all_pokemons_names = []
resulting_list = []
max_and_min_weight = []

def get_pokemons_with_double_a():
    url = "https://pokeapi.co/api/v2/pokemon/?limit=1000000"
    response = requests.get(url)
    all_pokemons.append(response.json().get('results'))
    for pokemon in all_pokemons[0]:
        all_pokemons_names.append(pokemon["name"])
    criteria_with_at = re.compile(".*at")
    filtered_list = list(filter(criteria_with_at.match, all_pokemons_names))
    for names in filtered_list:
        if names.count("a") >= 2:
            resulting_list.append(names)
    print(f"The total amount of pokemons with two As in their name, and the presence of 'at' is {len(resulting_list)}")

#get_pokemons_with_double_a()

def get_species_raichu_can_have_kids():
    """Given the case that there is no real specie given by the PokeAPI, what can be calculated is the amount of
    Pokemons that can have eggs with Raichu, which is what will be calculated over this method."""
    url = "https://pokeapi.co/api/v2/pokemon/raichu"
    response = requests.get(url)
    species_link = response.json().get("species")["url"]
    response = requests.get(species_link)
    species = response.json().get("egg_groups")
    for group in species:
        response = requests.get(group["url"])
        pokemons = response.json().get("pokemon_species")
        for pokemon in pokemons:
            all_pokemons_names.append(pokemon)

    print(len(all_pokemons_names))

#get_species_raichu_can_have_kids()

def max_and_min_fighting_poke_weight():
    url = "https://pokeapi.co/api/v2/type/fighting"
    response = requests.get(url)
    all_pokemons = response.json().get("pokemon")
    all_pokemon_weight = []
    for pokemon in all_pokemons:
        if int(pokemon["pokemon"]["url"].split('/')[6]) > 151:
            continue
        all_pokemons_names.append(pokemon["pokemon"]["name"])
    for pokemon in all_pokemons_names:
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
        response = requests.get(url)
        weight = response.json().get("weight")
        all_pokemon_weight.append(weight)
    max_and_min_weight.append(max(all_pokemon_weight))
    max_and_min_weight.append(min(all_pokemon_weight))
    print(max_and_min_weight)
    print(f"The maximum and minimum weight for the fighting type pokemons are {max_and_min_weight[0]} as max and {max_and_min_weight[1]} as min")

max_and_min_fighting_poke_weight()