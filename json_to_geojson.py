from sys import argv
from os.path import exists
import simplejson as json  # pip3 install simplejson

# run the script in terminal by doing `python3 json_to_geojson.py input_file.json output_file.json``
# script, in_file, out_file = argv
in_file = 'data/json_to_geojson/in/global.json'
out_file = 'data/json_to_geojson/out/global_geojson.json'

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
    if i["properties"]["commissioning_year"] == '':
        i["properties"]["commissioning_year"] = None
    else:
        year_int = int(float(i["properties"]["commissioning_year"]))
        i["properties"]["commissioning_year"] = year_int
    # replace keys where appropriate:
    i["properties"]['id'] = i["properties"].pop('gppd_idnr')
    # erase empty fields:
    delete_list = []
    for attribute, value in i["properties"].items():
        if value == "":
            delete_list.append(attribute)
    for attribute in delete_list:
        del i["properties"][attribute]
    # erase unwanted fields:
    unwanted = ['latitude', 'longitude', 'source', 'url', 'geolocation_source', 'wepp_id', 'estimated_generation_note_2012', 'estimated_generation_note_2013', 'estimated_generation_note_2014', 'estimated_generation_note_2015', 'estimated_generation_note_2016', 'estimated_generation_note_2017', 'estimated_generation_note_2018', 'estimated_generation_note_2019', 'estimated_generation_note_2020', 'estimated_generation_note_2021', 'estimated_generation_note_2022']
    for item in unwanted:
        if i["properties"].get(item) is not None:
            del i["properties"][item]  
        else:
            pass 


output = open(out_file, 'w')
json.dump(geojson, output)


