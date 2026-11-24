import requests


def get_brands(vehicleType):
    API_URL = f'https://fipe.parallelum.com.br/api/v2/{vehicleType}/brands'
    response = requests.get(API_URL)
    data = response.json()
    return data



