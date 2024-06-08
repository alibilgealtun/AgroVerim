import requests
from crop_profile import crop_profiles as cp
from city import get_lat_lon 
from keys import OPENWEATHER_API_KEY as api_key, MET_API_KEY as met_api_key
from datetime import datetime
from meteostat import Point,Daily

def get_air_quality(lat, lon):
    url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    
    if 'list' in data and len(data['list']) > 0:
        air_quality = {
            'pm2_5': data['list'][0]['components']['pm2_5'],
            'pm10': data['list'][0]['components']['pm10'],
            'o3': data['list'][0]['components']['o3'],
            'no2': data['list'][0]['components']['no2']
        }
    else:
        print(f"Error: Unexpected air quality data format: {data}")
        air_quality = {
            'pm2_5': None,
            'pm10': None,
            'o3': None,
            'no2': None
        }
    return air_quality

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
                pH = layer['depths'][0]['values']['mean']
            elif layer['name'] == 'ocd':
                organic_carbon = layer['depths'][0]['values']['mean']

    soil_data = {
        'organic_carbon': None,
        'pH': 7
    }

    return soil_data

def get_climate_data(lat, lon):
    start = datetime(2018, 1, 1)
    end = datetime(2018, 12, 31)

    # Create Point for Vancouver, BC
    location = Point(lat, lon)

    # Get daily data for 2018
    data = Daily(location, start, end)
    data = data.fetch()
    tavg_mean = data['tavg'].mean()

    climate_data = {
        'temperature' : round(tavg_mean,2)
    }
    return climate_data


def get_all_data(lat, lon):
    air_quality = get_air_quality(lat, lon)
    soil_data = get_soil_data(lat, lon)
    climate_data = get_climate_data(lat, lon)
    
    all_data = {
        'air_quality': air_quality,
        'soil_data': soil_data,
       'climate_data': climate_data
    }
    return all_data


def recommend_crops(data, crop_profiles):
    recommendations = []
    
    for crop, profile in crop_profiles.items():
        temp_min, temp_max = profile['temperature']
        #rain_min, rain_max = profile['rainfall']
        ph_min, ph_max = profile['ph']
        carbon_min, carbon_max = profile['organic_carbon']
        
        temp = data['climate_data']['temperature']
        #rain = data['climate_data']['rainfall']
        ph = data['soil_data']['pH']
        carbon = data['soil_data']['organic_carbon']
        
        if temp is not None and not (temp_min <= temp <= temp_max):
           continue
        #if rain is not None and not (rain_min <= rain <= rain_max):
           # continue
        if ph is not None and not (ph_min <= ph <= ph_max):
            continue
        if carbon is not None and not (carbon_min <= carbon <= carbon_max):
            continue
        
        recommendations.append(crop)
    
    return recommendations

city = input("Enter the city: ")

lat, lon = get_lat_lon(city, None)
print(f'Your lat: {lat}, your lon: {lon} ')

all_datas = get_all_data(lat, lon)

for i,j  in all_datas.items():
    print(f'{i}: {j}')
recommends = recommend_crops(all_datas,cp )

print(recommends)