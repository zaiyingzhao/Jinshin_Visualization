import jinshin_to_geojson_dictionary as jinshin
import pandas as pd

dic = jinshin.dic
tweets = pd.read_csv("tweets.csv")

line = []
station = []  # place
accidents = []
index = []

for i in range(len(tweets)):
    # 事故発生場所が線路上のとき
    if "〜" in tweets["place"][i]:
        nami = tweets["place"][i].find("〜")
        station1 = tweets["place"][i][:nami]
        station2 = tweets["place"][i][nami + 1 :]
        stations = [station1, station2]
    # 事故発生場所が駅のとき
    else:
        station1 = tweets["place"][i]
        stations = [station1]

    for sta in stations:
        # 既に同名駅で人身事故が発生している場合
        if sta in station:
            station_index = station.index(sta)
            # 路線名が一致している（完全に同じ駅）ときに人身事故回数加算
            if line[station_index] == dic[tweets["line"][i]]:
                accidents[station_index] += 1
                index[station_index].append(i)
            else:
                line.append(dic[tweets["line"][i]])
                station.append(sta)
                accidents.append(1)
                index.append([i])
                
                            
        # 同名駅で人身事故が発生していない場合
        else:
            line.append(dic[tweets["line"][i]])
            station.append(sta)
            accidents.append(1)
            index.append([i])

data = pd.DataFrame({"路線名": line, "駅名": station, "人身事故回数": accidents, "index": index})

data.to_csv("/home/zaiying/A-Pastani/data/accidents_per_station.csv", encoding="utf-8")
