from urllib import request
import requests

base_url = 'https://ghibliapi.herokuapp.com/'
endpoint = 'species'
final_url = base_url + endpoint

params_dict = {
    'fields':'name,hair_colors,eye_colors',
    'limit':10
    }

r = requests.get(final_url, params=params_dict)
print(r.url)