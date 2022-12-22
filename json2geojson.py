# run the script in terminal by doing python json2geojson.py input_file.json output_file.json

from sys import argv
from os.path import exists
import simplejson as json  # pip3 install simplejson

script, in_file, out_file = argv

data = json.load(open(in_file))

geojson = {
    "type": "FeatureCollection",
    "features": [
    {
        "type": "Feature",
        "geometry" : {
            "type": "Point",
            "coordinates": [d["lon"], d["lat"]],
            },
        "properties" : d,
     } for d in data]
}


output = open(out_file, 'w')
json.dump(geojson, output)

print(geojson)