from urllib.request import urlopen
import json
from dotenv import load_dotenv # pip3 install python-dotenv
import os


lng = 0.5
lat = 53
destination = "addresses.json"
load_dotenv()
token = os.environ.get("MAPBOX_TOKEN")

coordinates = [lng, lat] 

url = "https://api.mapbox.com/geocoding/v5/mapbox.places/-73.989,40.733.json?types=address&access_token=pk.eyJ1IjoianNjYXN0cm8iLCJhIjoiY2s2YzB6Z25kMDVhejNrbXNpcmtjNGtpbiJ9.28ynPf1Y5Q8EyB_moOHylw"

# store the response of URL
response = urlopen(url)


data_json = json.loads(response.read())
out_file = open(destination, "w")
json.dump(data_json, out_file, indent = 6)
out_file.close()

print(data_json)