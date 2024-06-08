
import ee
ee.Authenticate()
ee.Initialize(project='ee-alialttun')

import folium

def deforestation_monitoring(coordinates):
    try:
        if len(coordinates) < 3:
            raise ValueError("Polygon requires at least 3 points.")
        
        aoi = ee.Geometry.Polygon([coordinates])
        
        collection = ee.ImageCollection('LANDSAT/LC08/C01/T1_SR') \
            .filterDate('2015-01-01', '2020-12-31') \
            .filterBounds(aoi)
        
        image = collection.median()
        
        ndvi = image.normalizedDifference(['B5', 'B4']).rename('NDVI')
        
        ndvi_params = {
            'min': 0,
            'max': 1,
            'palette': ['brown', 'green']
        }
        
        map_id_dict = ee.Image(ndvi).clip(aoi).getMapId(ndvi_params)
        return map_id_dict
    except Exception as e:
        return str(e)
     
    # Define an area of interest (AOI) based on input coordinates
    aoi = ee.Geometry.Polygon([coordinates])
    
    # Load Landsat image collections
    collection = ee.ImageCollection('LANDSAT/LC08/C01/T1_SR') \
        .filterDate('2015-01-01', '2020-12-31') \
        .filterBounds(aoi)
    
    # Select the median image
    image = collection.median()
    
    # Calculate NDVI
    ndvi = image.normalizedDifference(['B5', 'B4']).rename('NDVI')
    
    # Define visualization parameters
    ndvi_params = {
        'min': 0,
        'max': 1,
        'palette': ['brown', 'green']
    }
    
    # Visualize NDVI
    ndvi_map = ee.Image(ndvi).clip(aoi)
    url = ndvi_map.getThumbUrl(ndvi_params)
    
    return "Deforestation Monitoring NDVI map URL: " + url



def air_quality_analysis(coordinates):
    ee.Initialize()
    
    # Define an area of interest (AOI) based on input coordinates
    aoi = ee.Geometry.Polygon([coordinates])
    
    # Load Sentinel-5P NO2 data
    collection = ee.ImageCollection('COPERNICUS/S5P/NRTI/L3_NO2') \
        .filterDate('2020-01-01', '2020-12-31') \
        .filterBounds(aoi)
    
    # Select the median image
    image = collection.median()
    
    # Define visualization parameters
    no2_params = {
        'min': 0,
        'max': 0.0002,
        'palette': ['blue', 'green', 'yellow', 'red']
    }
    
    # Visualize NO2
    no2_map = image.select('tropospheric_NO2_column_number_density').clip(aoi)
    url = no2_map.getThumbUrl(no2_params)
    
    return "Air Quality NO2 map URL: " + url


def water_quality_monitoring(coordinates):
    ee.Initialize()
    
    # Define an area of interest (AOI) based on input coordinates
    aoi = ee.Geometry.Polygon([coordinates])
    
    # Load Landsat image collections
    collection = ee.ImageCollection('LANDSAT/LC08/C01/T1_SR') \
        .filterDate('2020-01-01', '2020-12-31') \
        .filterBounds(aoi)
    
    # Select the median image
    image = collection.median()
    
    # Calculate NDWI
    ndwi = image.normalizedDifference(['B3', 'B5']).rename('NDWI')
    
    # Define visualization parameters
    ndwi_params = {
        'min': -1,
        'max': 1,
        'palette': ['brown', 'blue']
    }
    
    # Visualize NDWI
    ndwi_map = ee.Image(ndwi).clip(aoi)
    url = ndwi_map.getThumbUrl(ndwi_params)
    
    return "Water Quality NDWI map URL: " + url

def urban_heat_island(coordinates):
    ee.Initialize()
    
    # Define an area of interest (AOI) based on input coordinates
    aoi = ee.Geometry.Polygon([coordinates])
    
    # Load Landsat image collections
    collection = ee.ImageCollection('LANDSAT/LC08/C01/T1_SR') \
        .filterDate('2020-06-01', '2020-08-31') \
        .filterBounds(aoi)
    
    # Select the median image
    image = collection.median()
    
    # Calculate land surface temperature (LST)
    lst = image.select('B10').multiply(0.1).subtract(273.15).rename('LST')
    
    # Define visualization parameters
    lst_params = {
        'min': 20,
        'max': 40,
        'palette': ['blue', 'green', 'red']
    }
    
    # Visualize LST
    lst_map = ee.Image(lst).clip(aoi)
    url = lst_map.getThumbUrl(lst_params)
    
    return "Urban Heat Island LST map URL: " + url


def carbon_sequestration(coordinates):
    ee.Initialize()
    
    # Define an area of interest (AOI) based on input coordinates
    aoi = ee.Geometry.Polygon([coordinates])
    
    # Load biomass dataset
    biomass = ee.Image('NASA/ORNL/biomass_carbon_density/v1')
    
    # Clip the image to AOI
    biomass_clipped = biomass.clip(aoi)
    
    # Define visualization parameters
    biomass_params = {
        'min': 0,
        'max': 100,
        'palette': ['yellow', 'green', 'darkgreen']
    }
    
    # Visualize biomass
    url = biomass_clipped.getThumbUrl(biomass_params)
    
    return "Carbon Sequestration map URL: " + url


def agricultural_monitoring(coordinates):
    ee.Initialize()
    
    # Define an area of interest (AOI) based on input coordinates
    aoi = ee.Geometry.Polygon([coordinates])
    
    # Load Landsat image collections
    collection = ee.ImageCollection('LANDSAT/LC08/C01/T1_SR') \
        .filterDate('2020-05-01', '2020-09-30') \
        .filterBounds(aoi)
    
    # Select the median image
    image = collection.median()
    
    # Calculate NDVI
    ndvi = image.normalizedDifference(['B5', 'B4']).rename('NDVI')
    
    # Define visualization parameters
    ndvi_params = {
        'min': 0,
        'max': 1,
        'palette': ['brown', 'green']
    }
    
    # Visualize NDVI
    ndvi_map = ee.Image(ndvi).clip(aoi)
    url = ndvi_map.getThumbUrl(ndvi_params)
    
    return "Agricultural Monitoring NDVI map URL: " + url

def disaster_response(coordinates):
    ee.Initialize()
    
    # Define an area of interest (AOI) based on input coordinates
    aoi = ee.Geometry.Polygon([coordinates])
    
    # Load MODIS fire data
    collection = ee.ImageCollection('MODIS/006/MCD14DL') \
        .filterDate('2020-01-01', '2020-12-31') \
        .filterBounds(aoi)
    
    # Select the median image
    image = collection.median()
    
    # Define visualization parameters
    fire_params = {
        'min': 0,
        'max': 1,
        'palette': ['black', 'red', 'yellow']
    }
    
    # Visualize fire data
    fire_map = image.clip(aoi)
    url = fire_map.getThumbUrl(fire_params)
    
    return "Disaster Response Fire map URL: " + url


def main():
    print("Select a project to run:")
    print("1. Deforestation Monitoring")
    print("2. Air Quality Analysis")
    print("3. Water Quality Monitoring")
    print("4. Urban Heat Island Effect")
    print("5. Carbon Sequestration")
    print("6. Agricultural Monitoring")
    print("7. Disaster Response and Management")
    
    choice = int(input("Enter the number of the project: "))
    coordinates = input("Enter coordinates as a list of lists (e.g., [[-60.0, -10.0], [-60.0, -12.0], [-58.0, -12.0], [-58.0, -10.0]]): ")
    coordinates = eval(coordinates)  # Evaluate the input string to convert it into a list of lists
    try:
        map_id_dict = None
        if choice == 1:
            map_id_dict = deforestation_monitoring(coordinates)
        elif choice == 2:
            result = air_quality_analysis(coordinates)
        elif choice == 3:
            result = water_quality_monitoring(coordinates)
        elif choice == 4:
            result = urban_heat_island(coordinates)
        elif choice == 5:
            result = carbon_sequestration(coordinates)
        elif choice == 6:
            result = agricultural_monitoring(coordinates)
        elif choice == 7:
            result = disaster_response(coordinates)
        else:
            result = "Invalid choice."
        print(result)
    except:
       print("Error. Coordinates are wrong.")


    if isinstance(map_id_dict, dict):
        map = create_folium_map(map_id_dict, coordinates)
        map.save('map.html')
        print("Map has been saved to 'map.html'")
    else:
        print(map_id_dict)

if __name__ == "__main__":
    main()



