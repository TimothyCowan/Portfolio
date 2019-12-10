#!/usr/bin/python3
# import json
# import urllib.request
import webbrowser
import requests

NEO = 'https://api.nasa.gov/neo/rest/v1/feed?api_key='


def main():
    # getting my api key from saved document
    # commented out in favor of DEMO_KEY for rapid testing
    #    with open(r'C:\Users\Student\Documents\nasacreds.txt', 'r') as nc:
    #        myapikey = nc.read()
    # replace DEMO_KEY with myapikey when out of testing
    #    neo_resp = urllib.request.urlopen(NEO + "DEMO_KEY")
    #    neo_json = neo_resp.read().decode()
    #    neo_py = json.loads(neo_json)
    neo_py = requests.get(NEO + "DEMO_KEY").json()

    # variables to be used
    counter = 0
    dict_for_links = {}
    # makes menu options for user to pick asteroid from
    for nasadate in neo_py["near_earth_objects"]:
        print(f'-----{nasadate}-----')  # each date displayed followed by released astroid info
        counter_endof_dict = 0  # counter saves a value to assosiate the users menu selection w/ the number of that astroid specific to its release date ex: input of '55' ---> 2019-12-10   '1' 
        for astro in neo_py["near_earth_objects"][nasadate]:
            counter_endof_dict = counter_endof_dict + 1
            counter = counter + 1
            dict_for_links[counter] = (astro['name'], astro['nasa_jpl_url'])
            print('(', counter, ')', 'Name of Astroid: ' + astro['name'])
    your_asteroid = int(
        input(f"\nPlease select an astroid for more info(1-{counter}): "))  # dynamic prompt for astroid selection
    input(f"Press ENTER to open a browser tab for more information on asteroid:{dict_for_links[your_asteroid][0]}")
    webbrowser.open(dict_for_links[your_asteroid][1])


if __name__ == "__main__":
    main()
