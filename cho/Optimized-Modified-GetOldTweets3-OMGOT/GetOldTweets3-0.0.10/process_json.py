import json
import pickle

with open("datalist.pickle", "rb") as p:
    datalist = pickle.load(p)

with open("railname.pickle", "rb") as q:
    railname = pickle.load(q)

for i in range(len(datalist)):
    json_open = open(datalist[i], "r")
    rail_json = json.load(json_open)

    for j in range(len(rail_json["features"])):
        rail_json["features"][j]["properties"]["railname"] = railname[i]

    filename = datalist[i][:-8] + "_addRailname.geojson"

    with open(filename, "w") as f:
        json.dump(rail_json, f, ensure_ascii=False)
