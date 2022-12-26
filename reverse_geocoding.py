from urllib.request import urlopen
import json
from dotenv import load_dotenv # pip3 install python-dotenv
import os

### <!--- BEWARE OF API COST ---!> ###

# coordinates = 53.34927043775156, -6.231504071377264
lng = -6.231504071377264
lat = 53.34927043775156
in_file = 'test.geojson'
destination = "data/reverse_geocoding/out/addresses.geojson"
load_dotenv()
token = os.environ.get("MAPBOX_TOKEN")

# coordinates = [lng, lat] 

# get all coordinates from origin geojson file:
for i in in_file["features"]:
    # replace strings with integers where appropriate:
    coordinates = i["geometry"]["coordinates"]
    i["properties"]["capacity_mw"] = capacity_int
    year_int = int(float(i["properties"]["commissioning_year"]))
    i["properties"]["commissioning_year"] = year_int

"geometry": { "type": "Point", "coordinates": [-8.0752, 52.8301] },
for i in range(10):
    url = f"https://api.mapbox.com/geocoding/v5/mapbox.places/{lng},{lat}.json?types=address&access_token={token}"

    # store the response of URL
    response = urlopen(url)
    data_json = json.loads(response.read())

# dump data to json file
out_file = open(destination, "w")
json.dump(data_json, out_file, indent = 6)
out_file.close()




print(data_json)
# print("coordinates: ", coordinates)