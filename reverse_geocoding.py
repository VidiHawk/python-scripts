from urllib.request import urlopen
import json
from dotenv import load_dotenv # pip3 install python-dotenv
import os
import gc
import time


load_dotenv()
token = os.environ.get("MAPBOX_TOKEN")

### <!--- BEWARE OF API COST ---!> ###
### Mapbox's Temporary Geocoding API is free for up to 100,000 requests per month. 
### Prices start at $0.75/1,000 after that.


lng = -6.231504071377264
lat = 53.34927043775156
in_file = 'data/reverse_geocoding/global_geojson.json'
destination = "data/reverse_geocoding/global_geojson.json"
max_api_calls = 100000


def load_and_dump(index, api_calls):
    data_json = json.load(open(in_file))
    existing_addresses = 0
    for x in range(10):
        feat_json = data_json["features"][index]
        if "address" in feat_json["properties"]:
            existing_addresses +=1
            index += 1
            continue
        else:
            if "coordinates" in feat_json["geometry"]:
                coordinates = feat_json["geometry"]["coordinates"]
                lng = coordinates[0]
                lat = coordinates[1]
                api_calls += 1
                # fetch reverse geoding data based on coordinates
                url = f"https://api.mapbox.com/geocoding/v5/mapbox.places/{lng},{lat}.json?proximity={lng},{lat}&types=address&access_token={token}"
                '''the Geocoding API is limited to 600 requests per min.
                At 0.05 we are at 180 r/min and still experience throttling
                At 0.1 we are at 140 r/min and still experience throttling
                At 0.2 we are at 120 r/min and still experience throttling
                At 0.5 we are at 75 r/min 
                '''
                time.sleep(0.5) 
                try:
                    response = urlopen(url, timeout=5)
                except Exception:
                    print("TIMEOUT! sleeping for a minute...")
                    time.sleep(60)
                    continue 
                response_json = json.loads(response.read())
                # print(response_json)
                if response_json['features']:
                    if response_json['features'][0].get('place_name') is not None:
                        address = response_json['features'][0]['place_name']
                        data_json["features"][index]["properties"]["address"] = address
                        # print(address)
                else:
                    data_json["features"][index]["properties"]["address"] = "unknown"
                    # if "country_long" in i["properties"]:
                    #     print("no address found in ", i["properties"]["country_long"])
                if api_calls >= max_api_calls:
                    break
            else:
                print("no coordinates")
            index += 1
            del response, response_json
    # dump data to json file
    if existing_addresses != 10:
        out_file = open(destination, "w")
        json.dump(data_json, out_file, indent = 4)
        out_file.close()
        del out_file
    else:
        print("addresses already exists")
    del data_json
    gc.collect()
    return index, api_calls

index = 6450
api_calls = 0

for i in range(max_api_calls):
    index, api_calls = load_and_dump(index, api_calls)
    print("index ", index)
    print("api call ", api_calls)
    # if index % 1000 == 0:
    #     print(f"index: {index}, api calls: {api_calls}")
    #     input("Press any key to continue...")
        





