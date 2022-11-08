import subprocess
from subprocess import PIPE
import csv
import pandas as pd

# 今後以下の情報をcsvから読み取ってツイート数を取得
since = "2021-11-01 00:59:00"
until = "2021-11-01 01:00:00"
keyword = "京王線"

cp = subprocess.run(["python3","cli.py","-s",keyword,"--since",since,"--until",until],encoding="utf-8", stdout=PIPE)

with open("user.csv", "wt") as f:
    writer = csv.writer(f, lineterminator="\n")
    writer.writerow([cp.stdout])

# csvの行数確認
print(sum(1 for line in open("user.csv", "rb")))