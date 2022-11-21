import pandas as pd
import jinshin_to_geojson_dictionary as j

dic = j.dic

doors = pd.read_csv("/home/zaiying/A-Pastani/data/doorR2_addPath.csv")
doors = doors.sort_values("設置年月").reset_index(drop=True)

for i in range(len(doors)):
    index = doors["path"][i].rfind("/")
    doors["路線名"][i] = doors["path"][i][index+1:-20]

doors = doors[["路線名","駅名","設置年月"]]

doors.to_csv("/home/zaiying/A-Pastani/data/sorted_doordate.csv", encoding="utf-8_sig")