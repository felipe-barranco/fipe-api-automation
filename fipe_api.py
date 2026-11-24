import requests

def get_brand():
    API_URL = 'https://fipe.parallelum.com.br/api/v2/cars/brands'
    response = requests.get(API_URL)
    data = response.json()

get_brand()