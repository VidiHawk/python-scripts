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
            "coordinates": [d["longitude"], d["latitude"]],
            },
        "properties" : d,
     } for d in data]
}

# this loop will replace strings with integers:
for i in geojson["features"]:
    new_int = int(float(i["properties"]["capacity_mw"]))
    i["properties"]["capacity_mw"] = new_int


output = open(out_file, 'w')
json.dump(geojson, output)
