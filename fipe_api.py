import requests

def validate_response(response):
    response.raise_for_status()


def get_data(API_URL):
    response = requests.get(API_URL)
    validate_response(response)
    return response.json()


def get_brands(vehicle_type):
    API_URL = f'https://fipe.parallelum.com.br/api/v2/{vehicle_type}/brands'
    return get_data(API_URL)


def get_models(vehicle_type, brand_id):
    API_URL = f'https://fipe.parallelum.com.br/api/v2/{vehicle_type}/brands/{brand_id}/models'
    return get_data(API_URL)


def get_years(vehicle_type, brand_id, model_id):
    API_URL = f'https://fipe.parallelum.com.br/api/v2/{vehicle_type}/brands/{brand_id}/models/{model_id}/years'
    return get_data(API_URL)


def get_info(vehicle_type, brand_id, model_id, year_id):
    API_URL = f'https://fipe.parallelum.com.br/api/v2/{vehicle_type}/brands/{brand_id}/models/{model_id}/years/{year_id}'
    return get_data(API_URL)