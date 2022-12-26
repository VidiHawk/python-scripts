from urllib.request import urlopen
import json
from dotenv import load_dotenv # pip3 install python-dotenv
import os

load_dotenv()
token = os.environ.get("MAPBOX_TOKEN")

### <!--- BEWARE OF API COST ---!> ###
### Mapbox's Temporary Geocoding API is free for up to 100,000 requests per month. 
### Prices start at $0.75/1,000 after that.


lng = -6.231504071377264
lat = 53.34927043775156
in_file = 'data/reverse_geocoding/in/test.geojson'
destination = "data/reverse_geocoding/out/addresses_added.geojson"
max_api_calls = 10


data_json = json.load(open(in_file))

# get all coordinates from origin geojson file:
api_calls = 1
for i in data_json["features"]:
    # get coordinates from source file:
    coordinates = i["geometry"]["coordinates"]
    lng = coordinates[0]
    lat = coordinates[1]
    # fetch reverse geoding data based on coordinates
    url = f"https://api.mapbox.com/geocoding/v5/mapbox.places/{lng},{lat}.json?types=address&access_token={token}"
    response = urlopen(url)
    response_json = json.loads(response.read())
    print(response_json)
    if response_json['features']:
        if response_json['features'][0].get('place_name') is not None:
            address = response_json['features'][0]['place_name']
            i["properties"]["address"] = address
        else:
            i["properties"]["address"] = "unknown"
    else:
        pass
    print(address)
    print(api_calls)
    api_calls += 1
    if api_calls >= max_api_calls:
        break

# dump data to json file
out_file = open(destination, "w")
json.dump(data_json, out_file, indent = 6)
out_file.close()

