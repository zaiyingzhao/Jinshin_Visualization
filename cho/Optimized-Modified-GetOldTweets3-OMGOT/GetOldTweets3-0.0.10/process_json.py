import json

json_open = open("sample.geojson", "r")
rail_json = json.load(json_open)

# 型は辞書
# print(type(rail_json))

for i in range(len(rail_json["features"])):
    rail_json["features"][i]["properties"]["rail"] = "IGRいわて銀河鉄道"

with open("result.geojson", "w") as f:
    json.dump(rail_json, f, ensure_ascii=False)
