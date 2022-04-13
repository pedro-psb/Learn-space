from textwrap import indent
from os.path import exists
import requests
import json

def main():
    if exists('cats_facts.json'):
        facts = load_cats_text()
        print("# Facts gathered form 'cats_facts.json'")
        print()
    else:
        base_adress = 'https://cat-fact.herokuapp.com'
        endpoint = 'facts'
        json_data = get_resource(base_adress, endpoint)
        save_resource(json_data)
        
        facts = get_facts_from_json_repr(json_data)
        print("# Facts gathered from direct API call")
        print()

    for n in facts:
            print(n)



def get_resource(base_adress, endpoint):
    '''Returns a python repr of json'''
    adress = f'{base_adress}/{endpoint}'
    parameters = {}

    response = requests.get(adress, parameters)
    response.raise_for_status()
    requests.get()
    # A python representation of json with lists and dicts
    results = response.json()
    return results

def save_resource(results):
    '''Saves cats to a file "cats_facts.json"'''
    # A string representation of json
    results = json.dumps(results, indent=4)

    with open('cats_facts.json', 'w') as file:
        file.write(results)

def load_cats_text(file_name='cats_facts.json'):
    '''load a json and return a list of (str) facts'''
    with open(file_name) as file:
        # each line is an item in a list json_list
        # file_to_list = file.readlines()
        json_data = json.load(file)

    facts = get_facts_from_json_repr(json_data)
    return facts

def get_facts_from_json_repr(obj):
    return [n['text'] for n in obj]


if __name__ == "__main__":
    main()

