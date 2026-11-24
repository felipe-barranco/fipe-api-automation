import requests


def get_brands(vehicleType):
    API_URL = f'https://fipe.parallelum.com.br/api/v2/{vehicleType}/brands'
    response = requests.get(API_URL)
    data = response.json()
    return data


def get_models(vehicleType, brandId):
    API_URL = f'https://fipe.parallelum.com.br/api/v2/{vehicleType}/brands/{brandId}/models'
    response = requests.get(API_URL)
    data = response.json()
    return data


def get_years(vehicleType, brandId, modelId):
    API_URL = f'https://fipe.parallelum.com.br/api/v2/{vehicleType}/brands/{brandId}/models/{modelId}/years'
    response = requests.get(API_URL)
    data = response.json()
    return data


def get_price(vehicleType, brandId, modelId, yearId):
    API_URL = f'https://fipe.parallelum.com.br/api/v2/{vehicleType}/brands/{brandId}/models/{modelId}/years/{yearId}'
    response = requests.get(API_URL)
    data = response.json()
    return data