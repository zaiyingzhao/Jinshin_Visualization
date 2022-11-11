# 進捗
## day3(11/7)
アイデア出し
- 人口移動
  - 住民基本台帳人口移動報告( https://www.e-stat.go.jp/stat-search/files?page=1&toukei=00200523&tstat=000000070001 )とか使えそう

Twitter Developer Portalの登録

paper prototype作成
- 地図をズームしたときのイメージ
  - 画像は画像フォルダに
  - 去年のEKICHIKAを参考

![](shinchoku_image/kagaya/paper%20prototype.jpg)

## day4(11/8)
鉄道路線のgeojsonファイル489個を一つずつ手でダウンロードし、フォルダに整理した（これにほとんどの時間を費やした）

## day5(11/10)
QAR#5として時系列を操作するシークバーを折れ線グラフに対して実装した
- 現状はグラフ上を点が移動するのみ
  - もっとわかりやすい表示の仕方に変更したい

![](shinchoku_image/kagaya/Screenshot%20from%202022-11-10%2022-55-42.png)

- ver.2として自動再生機能とリアルタイムでのグラフの描画を実装した
  - Capstone Projectで利用できるくらいのものにはなった
  - なぜかグラフが下にもう一つ表示されてしまう

![](shinchoku_image/kagaya/Screenshot%20from%202022-11-11%2023-52-18.png)

ホームドア設置状況のエクセルファイルをcsv化し、設置日の表記を"Hyy.m"などから”yyyy/mm/dd"に変換した