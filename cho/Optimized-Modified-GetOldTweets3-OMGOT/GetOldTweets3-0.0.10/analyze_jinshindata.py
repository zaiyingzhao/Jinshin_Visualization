import pandas as pd
import datetime as dt

jinshindata = pd.read_csv("tweets.csv")

youbi = [0 for _ in range(7)]
month = [0 for _ in range(12)]
hour = [0 for _ in range(24)]

# jinshindata["date"][0] = dt.datetime.strptime(jinshindata["date"][0], "%Y/%m/%d %H:%M")
# print(jinshindata["date"][0].weekday())
for i in range(len(jinshindata)):
    youbi[dt.datetime.strptime(jinshindata["date"][i], "%Y/%m/%d %H:%M").weekday()] += 1
    month[dt.datetime.strptime(jinshindata["date"][i], "%Y/%m/%d %H:%M").month - 1] += 1
    hour[dt.datetime.strptime(jinshindata["date"][i], "%Y/%m/%d %H:%M").hour] += 1

youbi = pd.DataFrame(youbi, columns=["曜日"], index=["月", "火", "水", "木", "金", "土", "日"])
month = pd.DataFrame(
    month,
    columns=["月"],
    index=["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"],
)
hour = pd.DataFrame(
    hour,
    columns=["時(h)"],
    index=[
        "0時",
        "1時",
        "2時",
        "3時",
        "4時",
        "5時",
        "6時",
        "7時",
        "8時",
        "9時",
        "10時",
        "11時",
        "12時",
        "13時",
        "14時",
        "15時",
        "16時",
        "17時",
        "18時",
        "19時",
        "20時",
        "21時",
        "22時",
        "23時",
    ],
)

youbi.to_csv("/home/zaiying/A-Pastani/data/jinshin-youbi.csv")
month.to_csv("/home/zaiying/A-Pastani/data/jinshin-month.csv")
hour.to_csv("/home/zaiying/A-Pastani/data/jinshin-hour.csv")
