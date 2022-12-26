from urllib.request import urlopen
import json
from dotenv import load_dotenv # pip3 install python-dotenv
import os

# coordinates = 53.34927043775156, -6.231504071377264
lng = -6.231504071377264
lat = 53.34927043775156
destination = "data/addresses.json"
load_dotenv()
token = os.environ.get("MAPBOX_TOKEN")

# coordinates = [lng, lat] 


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