import random
import requests

def choose_pokemon():
    random_numbers = []
    for number in range(6):
        random_numbers.append(random.randint(1, 151))
    return random_numbers

pokemon_names = choose_pokemon()

def pokemons_to_choose():

    the_list_of_names = []
    for i in pokemon_names:
        url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(i)
        response = requests.get(url)
        pokemon = response.json()
        pokemons_charasteristics = {
            'id': pokemon['id'],
            'name': pokemon['name'],
            'height': pokemon['height'],
            'weight': pokemon['weight'],
            'base_experience': pokemon['base_experience']
        }
        the_list_of_names.append(pokemons_charasteristics)

    return the_list_of_names

print('You have drawn these six pokemons. You can see theirs ids and names: ')
for pokemon in pokemons_to_choose():
   print("name: {}, id: {}, weight: {}, base_experience {}, height: {}".format(pokemon['name'], pokemon['id'], pokemon['weight'], pokemon['base_experience'], pokemon['height']))

pokemonlist = open('pokemon.txt', 'w')

for x in range(len(pokemon)):
    pokemonlist.write(pokemon[x] + '\n')

pokemonlist.close()
