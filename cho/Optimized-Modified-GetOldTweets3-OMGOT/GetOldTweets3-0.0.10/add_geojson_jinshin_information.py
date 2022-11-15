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

# 全てのpropertiesにaccidentsとindex追加、NULL埋め
for i in range(len(station["features"])):
    station["features"][i]["properties"]["accidents"] = "NULL"
    station["features"][i]["properties"]["index"] = "NULL"

for i in range(len(station["features"])):
    flag = information["station"].isin(
        [station["features"][i]["properties"]["name"] + "駅"]
    )
    # geojsonの駅で人身事故が発生していないときは何もしない
    if sum(flag) == 0:
        continue

    # geojsonの駅で人身事故が発生していないときは何もしない
    flag = pd.DataFrame(flag)
    flagindex = flag[flag["station"] == True].index.tolist()

    # 同名の駅がある場合
    if len(flagindex) != 1:
        correctindex = -1
        for j in range(len(flagindex)):
            if (
                station["features"][i]["properties"]["railname"]
                == information["line"][flagindex[j]]
            ):
                correctindex = flagindex[j]
        if correctindex == -1:
            continue

        # 適切なindexを取得したのでpropertiesに情報追加
        station["features"][i]["properties"]["accidents"] = str(
            information["accidents"][correctindex]
        )
        station["features"][i]["properties"]["index"] = information["index"][
            correctindex
        ]

    # 同名の駅がない場合geojsonのpropetiesに情報追加
    else:
        station["features"][i]["properties"]["accidents"] = str(
            information["accidents"][flagindex[0]]
        )
        station["features"][i]["properties"]["index"] = information["index"][
            flagindex[0]
        ]

with open("/home/zaiying/A-Pastani/data/station_only_addJinshindata.geojson", "w") as f:
    json.dump(station, f, ensure_ascii=False)
