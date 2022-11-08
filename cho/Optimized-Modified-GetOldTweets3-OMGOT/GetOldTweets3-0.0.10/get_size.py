import subprocess
from subprocess import PIPE
import csv
import pandas as pd
from datetime import datetime as dt
import datetime
import time

start = time.time()
jinshin = pd.read_csv("jinshin2.csv")
tweets = []

for i in range(len(jinshin)):
    since = jinshin["date"][i] + ":00"
    since = dt.strptime(since, "%Y/%m/%d %H:%M:%S")
    keyword = jinshin["place"][i]
    until = since + datetime.timedelta(hours=2)
    since = since.strftime("%Y-%m-%d %H:%M:%S")
    until = until.strftime("%Y-%m-%d %H:%M:%S")
    cp = subprocess.run(
        ["python3", "cli.py", "-s", keyword, "--since", since, "--until", until],
        encoding="utf-8",
        stdout=PIPE,
    )

    with open("user.csv", "wt") as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerow([cp.stdout])

    # csvの行数確認
    size = sum(1 for line in open("user.csv", "rb"))
    print(i, size)
    tweets.append(size)

jinshin["tweets"] = tweets
jinshin.to_csv("tweets.csv")

print(time.time() - start)
