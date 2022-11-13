import pandas as pd
import pickle
import json

door = pd.read_csv("doorR2_addPath.csv")

with open("datalist.pickle", "rb") as p:
    datalist = pickle.load(p)

# 全てのaddRailname.geojsonのプロパティに"door"を加える（中身はNULL）
for i in range(len(datalist)):
    path = datalist[i][:-8] + "_addRailname.geojson"
    json_open = open(path, "r")
    rail_json = json.load(json_open)

    for j in range(len(rail_json["features"])):
        rail_json["features"][j]["properties"]["door"] = "NULL"

    with open(path, "w") as f:
        json.dump(rail_json, f, ensure_ascii=False)

for i in range(len(door)):
    if door["path"][i] == "NONE":
        continue
    try:
        json_open = open(door["path"][i], "r")
        rail_json = json.load(json_open)

        for j in range(len(rail_json["features"])):
            if rail_json["features"][j]["properties"]["name"] == door["駅名"][i]:
                rail_json["features"][j]["properties"]["door"] = door["設置年月"][i]

        with open(door["path"][i], "w") as f:
            json.dump(rail_json, f, ensure_ascii=False)

    except Exception as e:
        print(e)
