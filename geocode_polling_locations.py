import csv
import json
import pprint
from collections import OrderedDict


import geocode_request

index = 0
# with open('polling_locations_2011.csv','rb') as csvFile:
with open('polling_locations_2011.json','r') as in_f:
    with open('polling_results_2011.json','w') as out_f:
        with open('count.txt', 'r+') as count_f:
            georeader = json.load(in_f)
            geoJSONArray = []
            errors = []
            while index < 3000 : # Google's Daily Geocoder Limit
                try:
                    print "trying entry number " + str(index) + ": " + str(georeader[index]["address"])
                    response = json.loads(geocode_request.googleRequest(georeader[index]["address"]))
                    lat = response["results"][0]["geometry"]["location"]["lat"]
                    long = response["results"][0]["geometry"]["location"]["lng"]
                    # Enter the result into the output dictionary

                    geoOutput = OrderedDict()
                    geoOutput["type"] = "Feature"
                    geoOutput["geometry"] = {}
                    geoOutput["geometry"]["type"] = "Point"
                    geoOutput["geometry"]["coordinates"] = [long,lat]
                    geoOutput["properties"] = georeader[index]
                    geoJSONArray.append(geoOutput)

                    count_f.write("Last index," + str(index)+ ",Failues," + str(errors))
                    index += 1
                except:
                    errors.append(index)
                    count_f.write("Last index," + str(index)+ ",Failues," + str(errors))
                    index += 1

                    print "Failure. index is set to: " + str(index)
            json.dump(geoJSONArray, out_f)
