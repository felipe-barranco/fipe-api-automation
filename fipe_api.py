import requests

def get_brand():
    API_URL = 'https://fipe.parallelum.com.br/api/v2/cars/brands'
    response = requests.get(API_URL)
    data = response.json()

    brands = []
    for i in range(len(data)):
        brands.append(data[i]['name'])
    return brands


get_brand()