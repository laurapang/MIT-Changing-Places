# { "type": "Feature", "id": "AD", "properties": { "LAT": 42.54621238, "LON": 1.60028625 }, "geometry": { "type": "Point", "coordinates": [ 1.600286250000011, 42.546212380000043 ] } },

import csv
import os

with open('../../CDR/towers.csv', 'rU') as towers_file:
  with open('./nodes_towers.geojson', "a") as towers_geo:
    towers_geo.write("{\"type\": \"FeatureCollection\", \"features\": [");
    towers_reader = csv.reader(towers_file)
    for tower_row in towers_reader:
        tower_id = tower_row[0]
        latitude = tower_row[1]
        longitude = tower_row[2]
        towers_geo.write("{ \"type\": \"Feature\", \"id\": \"" + tower_id + "\", \"properties\": { \"LAT\": " + latitude + ", \"LON\": " + longitude +
                      " }, \"geometry\": { \"type\": \"Point\", \"coordinates\": [ " + longitude + ", " + latitude + " ] } },")
    towers_geo.seek(-1, os.SEEK_END)
    towers_geo.truncate()
    towers_geo.write("]}")