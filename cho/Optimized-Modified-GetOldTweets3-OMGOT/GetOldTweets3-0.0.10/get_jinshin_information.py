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
            station_index = [j for j, x in enumerate(station) if x == sta]
            # 路線名が一致している（完全に同じ駅）ときに人身事故回数加算
            flag = 1
            for idx in station_index:
                if type(line[idx]) == str: linelist1 = [line[idx]]
                elif type(line[idx]) != str: linelist1 = line[idx]
                if type(dic[tweets["line"][i]]) == str: linelist2 = [dic[tweets["line"][i]]]
                elif type(dic[tweets["line"][i]]) != str: linelist2 = dic[tweets["line"][i]]
                lineand = set(linelist1) & set(linelist2)
                if len(lineand) > 0:
                    accidents[idx] += 1
                    index[idx].append(i)
                    flag = 0
                    
            if flag:
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
data.to_csv("accidents_per_station.csv", encoding="utf-8")
