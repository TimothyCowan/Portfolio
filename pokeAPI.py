#!/usr/bin/python3
import requests


def main():
    poke_request = 'https://pokeapi.co/api/v2/pokemon-habitat/'
    pokejson = (requests.get(poke_request)).json()
    for area in pokejson['results']:  # prints each habitat
        print('>>', area['name'], '<<')
        area_lookup = (requests.get(area['url'])).json()

        for pokemon in area_lookup['pokemon_species']:
            print('   -', pokemon['name'])


if __name__ == "__main__":
    main()
