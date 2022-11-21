# 進捗
## day3(11/7)
- アイデア出し
  - 人口移動
    - 住民基本台帳人口移動報告( https://www.e-stat.go.jp/stat-search/files?page=1&toukei=00200523&tstat=000000070001 )とか使えそう

- Twitter Developer Portalの登録

- paper prototype作成
  - 地図をズームしたときのイメージ
  - 去年のEKICHIKAを参考

![](shinchoku_image/kagaya/paper%20prototype.jpg)

## day4(11/8)
- 鉄道路線のgeojsonファイル489個を一つずつ手でダウンロードし、フォルダに整理した（これにほとんどの時間を費やした）

## day5(11/10)
- QAR#5として時系列を操作するシークバーを折れ線グラフに対して実装した
  - ver.1はグラフ上を点が移動するのみ
   ![](shinchoku_image/kagaya/Screenshot%20from%202022-11-10%2022-55-42.png)

- ver.2として自動再生機能とリアルタイムでのグラフの描画を実装した
  - 参考：https://d3-graph-gallery.com/graph/area_basic.html, https://bl.ocks.org/officeofjane/47d2b0bfeecfcb41d2212d06d095c763
  - Capstone Projectで利用できるくらいのものにはなった
  - なぜかグラフが下にもう一つ表示されてしまう
  ![](shinchoku_image/kagaya/Screenshot%20from%202022-11-14%2013-03-52.png)

- ホームドア設置状況のエクセルファイルをcsv化し、設置日の表記を"Hyy.m"などから”yyyy/mm/dd"に変換した

## day6(11/14)
- 曜日別事故発生件数のヒストグラムを作成した
- 事故データを曜日別に分け、時計で表示しやすい形式にまとめた
  - データ加工は中村くんの[dataextract.ipynb](https://github.com/InfovisHandsOn/A-Pastani/blob/main/nakamura/dataextract.ipynb)を参考にし、一部を書き換えて行った
- 曜日を選択することで、時計に表示するデータを切り替えられるようにした
- 時計とヒストグラムと連携できるようにした
   ![](shinchoku_image/kagaya/Screenshot%20from%202022-11-14%2023-04-04.png)

## day7(11/15)
- ズーム機能を実装した
  - ボタンによるズームの実装を試みたが、ボタンでズームした後に地図を移動させようとするとズームが元に戻ってしまうバグが修正できず、断念した
- ヒストグラムの何もないところをクリックすると全データの表示に戻る機能を実装した
- ホームドア設置状況のグラフを実装した
  - ホームドア設置状況のcsvから累積設置数を抜き出したcsvを作成
  - グラフの描画とシークバーとの連動はday5のQARを利用した

## day8(11/21)
- ホームドアが設置された駅の地図上での見た目の変化を実装した
  - はじめは描画のたびに設置駅の座標をgeojsonファイルから検索する方法で実装したが、処理が重くなりすぎて断念
  - あらかじめ設置駅の緯度経度をgeojsonから抜き出したcsvを作成することにした
  - fillしたcircleを重ねるとマウスオーバーしたときにツールチップが出なくなってしまうが、circleのstrokeだけ描画することで回避した
