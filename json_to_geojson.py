from sys import argv
from os.path import exists
import simplejson as json  # pip3 install simplejson

# run the script in terminal by doing `python3 json_to_geojson.py input_file.json output_file.json``
# script, in_file, out_file = argv
in_file = 'data/json_to_geojson/in/test.json'
out_file = 'data/json_to_geojson/out/test.geojson'

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


for i in geojson["features"]:
    # replace strings with integers where appropriate:
    capacity_int = int(float(i["properties"]["capacity_mw"]))
    i["properties"]["capacity_mw"] = capacity_int
    year_int = int(float(i["properties"]["commissioning_year"]))
    i["properties"]["commissioning_year"] = year_int
    

    


output = open(out_file, 'w')
json.dump(geojson, output)
