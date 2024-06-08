from geopy.geocoders import Nominatim

def get_lat_lon(city, country=None):
  """
  This function uses Nominatim geocoder to retrieve latitude and longitude
  based on city and optional country information.

  Args:
      city (str): Name of the city.
      country (str, optional): Country of the city (defaults to None).

  Returns:
      tuple: A tuple containing latitude (float) and longitude (float),
              or None if location not found.
  """
  geolocator = Nominatim(user_agent="AgroVerim")  
  if country:
    location_str = f"{city}, {country}"
  else:
    location_str = city
  location = geolocator.geocode(location_str)
  if location:
    return location.latitude, location.longitude
  else:
    print(f"Location '{location_str}' not found.")
    return None

