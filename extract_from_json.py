from sys import argv
from os.path import exists
import simplejson as json  # pip3 install simplejson

# run the script in terminal by doing `python3 json_to_geojson.py input_file.json output_file.json``
# script, in_file, out_file = argv
in_file = 'data/json_to_geojson/in/test.json'
out_file = 'data/json_to_geojson/out/test.geojson'

data = json.load(open(in_file))


