import pandas as pd
import pickle

line = pd.read_csv("line.csv", encoding="shift_jis")
line = line[["jinshin", "geojson"]]

dict = {}
for i in range(len(line)):
    if line["geojson"][i] == "・":
        dict[line["jinshin"][i]] = "NULL"
    else:
        dict[line["jinshin"][i]] = line["geojson"][i]

with open("line_dict.pickle", "wb") as p:
    pickle.dump(dict, p)
