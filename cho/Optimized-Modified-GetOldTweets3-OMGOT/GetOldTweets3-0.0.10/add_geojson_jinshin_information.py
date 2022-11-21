import pandas as pd
import json

information = pd.read_csv("/home/zaiying/A-Pastani/data/accidents_per_station.csv")

json_open = open("/home/zaiying/A-Pastani/data/station_only.geojson")
station = json.load(json_open)
# print(station["features"][0]["properties"]["name"])

information = information.rename(
    columns={
        "Unnamed: 0": "idx",
        "路線名": "line",
        "駅名": "station",
        "人身事故回数": "accidents",
    }
)

station_ichiran = []
for i in range(len(station["features"])):
    station_ichiran.append(station["features"][i]["properties"]["name"])
# station_ichiran = pd.DataFrame(station_ichiran, columns={"station"})

# 全てのpropertiesにaccidentsとindex追加、NULL埋め
for i in range(len(station["features"])):
    station["features"][i]["properties"]["accidents"] = "NULL"
    station["features"][i]["properties"]["index"] = "NULL"

for i in range(len(information)):
    print(i)
    indexlist = [j for j, x in enumerate(station_ichiran) if x == information["station"][i][:-1]]
    
    # 同名の駅がある場合
    if len(indexlist) != 1:
        correctindex = -1
        for j in range(len(indexlist)):
            if (
                station["features"][indexlist[j]]["properties"]["railname"]
                == information["line"][i]
            ):
                correctindex = indexlist[j]
        if correctindex == -1:
            continue

        # 適切なindexを取得したのでpropertiesに情報追加
        station["features"][correctindex]["properties"]["accidents"] = str(information["accidents"][i])
        station["features"][correctindex]["properties"]["index"] = information["index"][i]

    # 同名の駅がない場合geojsonのpropetiesに情報追加
    else:
        station["features"][indexlist[0]]["properties"]["accidents"] = str(
            information["accidents"][i]
        )
        station["features"][indexlist[0]]["properties"]["index"] = information["index"][i]

with open("station_only_addJinshindata.geojson", "w") as f:
    json.dump(station, f, ensure_ascii=False)
