import requests


def validate_response(response):
    response.raise_for_status()


def get_brands(vehicle_type):
    API_URL = f'https://fipe.parallelum.com.br/api/v2/{vehicle_type}/brands'
    response = requests.get(API_URL)
    validate_response(response)
    data = response.json()
    return data


def get_models(vehicle_type, brand_id):
    API_URL = f'https://fipe.parallelum.com.br/api/v2/{vehicle_type}/brands/{brand_id}/models'
    response = requests.get(API_URL)
    validate_response(response)
    data = response.json()
    return data


def get_years(vehicle_type, brand_id, model_id):
    API_URL = f'https://fipe.parallelum.com.br/api/v2/{vehicle_type}/brands/{brand_id}/models/{model_id}/years'
    response = requests.get(API_URL)
    validate_response(response)
    data = response.json()
    return data


def get_info(vehicle_type, brand_id, model_id, year_id):
    API_URL = f'https://fipe.parallelum.com.br/api/v2/{vehicle_type}/brands/{brand_id}/models/{model_id}/years/{year_id}'
    response = requests.get(API_URL)
    validate_response(response)
    data = response.json()
    return data