import requests
from crop_profile import crop_profiles as cp
from city import get_lat_lon 
from keys import OPENWEATHER_API_KEY as api_key, MET_API_KEY as met_api_key
from datetime import datetime
from meteostat import Point,Daily

def get_soil_data(lat, lon):
    url = f"https://rest.isric.org/soilgrids/v2.0/properties/query?lat={lat}&lon={lon}"
    headers = {
        'accept': 'application/json',
    }
    response = requests.get(url, headers=headers)
    data = response.json()

    # Extracting pH (phh2o) and organic carbon (ocd) data
    pH = None
    organic_carbon = None
    if 'properties' in data:
        layers = data['properties']['layers']
        for layer in layers:
            if layer['name'] == 'phh2o':
                print(layer)
                pH = layer['depths'][0]['values']['mean']
            elif layer['name'] == 'ocd':
                organic_carbon = layer['depths'][0]['values']['mean']

    soil_data = {
        'organic_carbon': organic_carbon,
        'pH': pH
    }

    return soil_data

lat = 38.23166
lon = 27.02297
print(get_soil_data(lat, lon))