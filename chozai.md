# 趙在瀛進捗記録  
## 第3回（11/07）  
### テーマについて  
1. 以前に出したアイデア  
- ウェブブラウザの勢力図変遷
- SEO(search engine optimization)の複雑な要素を可視化
- 何らかの条件が与えられたときの最適な結果を可視化
- ハザードマップに犯罪率などの他の要素を加えた住みよい街マップ
- 行きたい場所の属性を選択するとおすすめの旅行先を提案するマップ
- 苗字の時代変遷（地域を絡める）
2. 今日出したアイデア  
- イベントで必要な物資から経済効果を算出し可視化する（様々なジャンルに経済効果は波及する）(https://www.soumu.go.jp/toukei_toukatsu/data/io/hakyu.htm)

- 世界の人口推移に加えて国を選択した時にその年代の死因を確認できるようなサイト

**→データの数や可視化のバリエーションからテーマを鉄道人身事故の可視化に決定（前回提案されたアイデア）**

### その他進捗
Twitter API登録（人身事故のimpactとして関連ツイート数を利用したい）  
Paper Prototype作成（駅をタップした時の画像/説明担当）

### 今後の流れ
**とりあえず自分は関連ツイート数の分析を担当に進めていく**   
tweepyを用いるにはTwitter APIのElevated access権限を取得する必要があり(現在はEssential)、Elevated access権限の申請を行った   
（申請の際に具体的なTwitter APIの利用方法や得た情報をどこまで公開する予定かなどを詳細に記述する必要があったので、認証されるのに少し時間がかかるかもしれない）  

**[追記]  
twitter APIでキーワードを含むツイート検索をしても取得できるツイート数に制限があるらしい（100件）  
また特定キーワードを含むツイート数を取得するにはacademic research accessが必要らしいがこれは一般学生には付与されない模様（[aquire_tweets.py](https://github.com/InfovisHandsOn/A-Pastani/blob/main/cho/acquire_tweets.py)のコメント参照）**  

## 第4回（11/08）
### 方針について  
今回のテーマでは過去12年までのツイートを取得できるようにする必要があるため、twitter APIを用いたツイート取得は困難と判断した  
**他の方法を色々調査した結果、GetOldTweetsモジュール(GOT)を利用することにした[^1]** ([参考記事](https://qiita.com/haniokasai/items/9eba9e232a144a0f8805)/[github](https://github.com/marquisvictor/Optimized-Modified-GetOldTweets3-OMGOT))  
[^1]: 正確にはtwitter API v2が公開されてからGetOldTweetsモジュールもほとんど使えない状態になっており、今回はtwitter API v2に対応した改良版GetOldTweets（OMGOT）を使う  

### 人身事故関連のツイート取得
- choディレクトリにGOTをクローンし、[cho/Optimized-Modified-GetOldTweets3-OMGOT/GetOldTweets3-0.0.10/cli.py](https://github.com/InfovisHandsOn/A-Pastani/blob/main/cho/Optimized-Modified-GetOldTweets3-OMGOT/GetOldTweets3-0.0.10/cli.py)を修正することで過去のツイート取得が可能であることを確認した  
- 続いてGetOldTweets3-0.0.10ディレクトリに[get_size.py](https://github.com/InfovisHandsOn/A-Pastani/blob/main/cho/Optimized-Modified-GetOldTweets3-OMGOT/GetOldTweets3-0.0.10/get_size.py)を追加し、中村くんがスクレイピングした人身事故データのcsvファイル([jinshin.csv](https://github.com/InfovisHandsOn/A-Pastani/blob/main/cho/Optimized-Modified-GetOldTweets3-OMGOT/GetOldTweets3-0.0.10/jinshin.csv))から必要な情報を取得/整形して人身事故関連ツイートを取得できるようにした 
- 試しに人身事故データcsvの頭10行を抽出したcsvファイル([jinshin2.csv](https://github.com/InfovisHandsOn/A-Pastani/blob/main/cho/Optimized-Modified-GetOldTweets3-OMGOT/GetOldTweets3-0.0.10/jinshin2.csv))にツイート件数取得を行った結果を[tweets.csv](https://github.com/InfovisHandsOn/A-Pastani/blob/main/cho/Optimized-Modified-GetOldTweets3-OMGOT/GetOldTweets3-0.0.10/tweets.csv)に格納した（元ファイルに'tweets'カラムを追加した形式）
- 現在は全データ（約15000件）に対してツイート件数取得を行っているが、ツイート数取得に人身事故1件あたり2秒ほどかかるため、実行に10時間ほどかかる計算になる（現在実行中）

### 今後の流れ
次回までに関連ツイート数の分析は終わると考えられるため、今後は他2人と合流して実際の可視化の部分に着手することになるはず

## 第5回（11/10）
### やったこと
- ツイート数取得を完了した（[tweets.csv](https://github.com/InfovisHandsOn/A-Pastani/blob/main/data/tweets.csv)）
- 同名の駅を区別するために全ての鉄道のgeojsonのpropertiesに路線名を追加した。
  1. 中村くんが[全てのgeojsonパスのリスト](https://github.com/InfovisHandsOn/A-Pastani/blob/main/home/datalist.js)を作成してくれていたので、[getAbsolutePath.py](https://github.com/InfovisHandsOn/A-Pastani/blob/main/cho/Optimized-Modified-GetOldTweets3-OMGOT/GetOldTweets3-0.0.10/getAbsolutePath.py)でそのパスから路線名を抽出した上で自身の環境の絶対パスに整形した
  2. [process_json.py](https://github.com/InfovisHandsOn/A-Pastani/blob/main/cho/Optimized-Modified-GetOldTweets3-OMGOT/GetOldTweets3-0.0.10/process_json.py)で先ほど整形した絶対パスのリストを用いて全てのgeojsonにアクセスし、propertiesに該当路線名を追加した([data](https://github.com/InfovisHandsOn/A-Pastani/tree/main/data)/各路線ディレクトリの"路線名_addRailname.geojson")
  3. [路線名の情報](https://github.com/InfovisHandsOn/A-Pastani/blob/main/data/railname.pickle)は実際に同名駅の区別に使うと思われたのでpickleファイルの形で格納した
- 後々必要になるかもしれないと思ったので[analyze_jinshindata.py](https://github.com/InfovisHandsOn/A-Pastani/blob/main/cho/Optimized-Modified-GetOldTweets3-OMGOT/GetOldTweets3-0.0.10/analyze_jinshindata.py)で人身事故データを分析し、[曜日別](https://github.com/InfovisHandsOn/A-Pastani/blob/main/data/jinshin-youbi.csv)/[月別](https://github.com/InfovisHandsOn/A-Pastani/blob/main/data/jinshin-month.csv)/[時間別](https://github.com/InfovisHandsOn/A-Pastani/blob/main/data/jinshin-hour.csv)の人身事故発生数をcsvファイルとして追加した
- QRA#5で画面の移動やズームを担当することになったので、簡易的にこれらを実装した（GitHubにはまだ載せていません）

### 次回までにやること
- QRA#5の改善
  - 現在ズームはマウス位置取得したうえでそのマウス位置を中心として画面拡大するという方法でやっているが、Capstone Projectでは駅をクリックしたときに駅に向かってズームするということをしたいので、少し実装を変える必要がある
  - またtransition()を用いているもののまだクオリティが低い感じがするので、ズーム時のエフェクト/滑らかさにもう少しこだわりたい
- 人身事故発生場所が線路上（踏切など）のときの対応
  - チーム全体の課題にはなるが人身事故発生場所が曖昧なときにどのように可視化を行うか考えたい
  - 個人的には線路上の踏切の情報を探してきて、該当駅間の踏切を事故現場とすればいいのではと思っている

## 第6回（11/14）
### やったこと
- 取得した[ホームドア設置日時のcsv](https://github.com/InfovisHandsOn/A-Pastani/blob/main/data/doorR2_converted.csv)からすべてのgeojsonのpropertiesにホームドア設置日時を示す"door"プロパティを追加した。
  1. ホームドア設置日時のcsvに表示されている事業所名/路線名のパスと実際にgeojsonにアクセスするために必要なパスが全く一致していなかったため、（力技にはなってしまうが）それぞれの対応を確認したうえで[get_correct_path.py](https://github.com/InfovisHandsOn/A-Pastani/blob/main/cho/Optimized-Modified-GetOldTweets3-OMGOT/GetOldTweets3-0.0.10/get_correct_path.py)において当該のgeojsonにアクセスできるように前処理した（[パスを加えたcsvファイル](https://github.com/InfovisHandsOn/A-Pastani/blob/main/data/doorR2_addPath.csv)） 
  2. [add_doordate_to_geojson.py](https://github.com/InfovisHandsOn/A-Pastani/blob/main/cho/Optimized-Modified-GetOldTweets3-OMGOT/GetOldTweets3-0.0.10/add_doordate_to_geojson.py)実際にそれぞれのホームドア設置情報に関して該当geojsonにアクセスし、"door"プロパティを追加したうえで設置日時情報を追加した（ホームドアが現在設置されていない駅に関しては"NULL"埋めをした）
  3. ホームドア設置日時の情報は前回追加した路線情報のadd_Railname.geojsonに上書きする形をとった
- 実際に人身事故の情報と実際の場所を紐づけるときに人身事故が起こった路線名とgeojsonに追加した路線名が一致している必要があるが、実際にはまったく一致していない。よって人身事故発生路線を入力するとgeojsonに追加した正式な路線名を返す辞書の作成を行った
  1. （とても力技になるが）人身事故発生路線名と対応する正式路線名を横並びにした[excelファイル](https://github.com/InfovisHandsOn/A-Pastani/blob/main/data/line.csv)を作成した（最低限sortをするなどの工夫は行った）
  2. [make_dict.py](https://github.com/InfovisHandsOn/A-Pastani/blob/main/cho/Optimized-Modified-GetOldTweets3-OMGOT/GetOldTweets3-0.0.10/make_dict.py)にてexcelファイルを読み込み必要な形の辞書に整形して[pickleファイル](https://github.com/InfovisHandsOn/A-Pastani/blob/main/data/line_dict.pickle)として保存した
- QRA#5の完成
  - ズーム及びズームリセットを実装した
  - [提出ファイル](https://github.com/InfovisHandsOn/A-Pastani/blob/main/cho/QRA5/index.html)の県をクリックするとクリックした位置を中心としてズームが行われ、リセットボタンを押すと元の位置/縮尺に戻るようになっている
- **[路線辞書について追記]** 人身事故情報で路線名に愛称（地元で使われる正式ではない名称）が使われている場合についても1つ1つ調べて追加した。またpickleファイル形式だと使いづらい気がしたので[辞書を定義するだけのファイル](https://github.com/InfovisHandsOn/A-Pastani/blob/main/data/jinshin_to_geojson_linename_dic.py)を追加した。

## 第7回（11/15）
### やったこと
- 前回追加した路線辞書を用いて地図上の駅と人身事故情報の紐づけを行うことで判明したデータ不足（[このコミット履歴](https://github.com/InfovisHandsOn/A-Pastani/commit/b07c35f88b27938d8dfa442c0da9f07510d62869)など）をふまえ辞書のキー追加を行った（これでほぼすべての人身事故情報の紐づけができることになる）
- 新たに追加した4つのgeojsonに対して第5/6回に行った路線名/ホームドア設置日時プロパティを追加した
- [index.html](https://github.com/InfovisHandsOn/A-Pastani/blob/main/home/index.html)にズーム機能と簡易的なツールチップ表示機能を追加した
  - QRA#5の実装をcapstone projectに適用した形
- geojsonから人身事故情報にアクセスできるようにした
  1. [get_jinshin_information.py](https://github.com/InfovisHandsOn/A-Pastani/blob/main/cho/Optimized-Modified-GetOldTweets3-OMGOT/GetOldTweets3-0.0.10/get_jinshin_information.py)において、[人身事故データ](https://github.com/InfovisHandsOn/A-Pastani/blob/main/data/tweets.csv)と以前作成した[人身事故データの路線名から正式路線名を返す辞書](https://github.com/InfovisHandsOn/A-Pastani/blob/main/cho/Optimized-Modified-GetOldTweets3-OMGOT/GetOldTweets3-0.0.10/jinshin_to_geojson_dictionary.py)を用いて各駅の人身事故回数およびその人身事故のcsvデータにおけるインデックスを取得した（[accidents_per_station.csv](https://github.com/InfovisHandsOn/A-Pastani/blob/main/cho/Optimized-Modified-GetOldTweets3-OMGOT/GetOldTweets3-0.0.10/accidents_per_station.csv)）
  2. [add_geojson_jinshin_information.py](https://github.com/InfovisHandsOn/A-Pastani/blob/main/cho/Optimized-Modified-GetOldTweets3-OMGOT/GetOldTweets3-0.0.10/add_geojson_jinshin_information.py)において中村くんが作成した[すべての駅情報をまとめたgeojson](https://github.com/InfovisHandsOn/A-Pastani/blob/main/data/station_only.geojson)の全ての駅に対して事故回数と該当インデックスのプロパティを追加した（[station_only_addJinshindata.geojson](https://github.com/InfovisHandsOn/A-Pastani/blob/main/data/station_only_addJinshindata.geojson)）
  - これによってgeojsonから事故詳細を参照できるようになり、tooltipに反映させる予定

## 第8回（11/21）
### やったこと
- tooltip実装
  - 以前geojsonに加えた様々なpropertiesを参照して事故情報やホームドア設置日時などをホバー時に表示できるようにした
  - 事故のニュース原文についてはtooltipにurlを表示し、そこから当該サイトに飛べるようにした
  - 被害情報やホームドア設置日時についてgeojsonに記載がない場合や人身事故回数が複数回の場合についても不自然でない表記になるよう注意した
- 加賀谷くんがホームドア設置日時以降の駅アイコン変更を実装する際に必要となる情報を抽出した[csv](https://github.com/InfovisHandsOn/A-Pastani/blob/main/data/sorted_doordate.csv)を作成した
- 路線名誤表示を修正
  - index.htmlでは二分探索をする便宜上で事故情報csvのインデックスを逆転させており、geojsonに追加したindexを逆転させずそのまま用いることで全く別の路線名が表示される不具合が発生していたため、これを解決した
- 同名駅の衝突によるバグ解消
  - 同名の駅があることによりtooltipに表示される路線名が入れ替わってしまうバグが確認されたので、以前作成した[add_geojson_jinshin_information.py](https://github.com/InfovisHandsOn/A-Pastani/blob/main/cho/Optimized-Modified-GetOldTweets3-OMGOT/GetOldTweets3-0.0.10/add_geojson_jinshin_information.py)を修正することでgeojson内のindex(事故情報csvの参照に用いる)を正しく更新した
- 駅アイコンクリック時にアイコンが点滅するようにした

## 第9回（11/22）
### やったこと
- 事故回数バグfix
  - 都内の事故回数があまりにも少ないことから確認したところ人身事故回数が正しく数えられていない場合があったので以前作成した[get_jinshin_information.py](https://github.com/InfovisHandsOn/A-Pastani/blob/main/cho/Optimized-Modified-GetOldTweets3-OMGOT/GetOldTweets3-0.0.10/get_jinshin_information.py)を修正して正確な事故回数をgeojsonへ書き込みした
  - 完成版index.htmlを全体的に確認したところtooltip表示、事故回数に対応する円サイズ、事故詳細サイトでの記載内容に一貫していない部分は見られていないのでこれで自身の担当箇所のバグは解消されたと思われる
  - (※一部一見事故回数に対応する円サイズが正しくない駅が見られるが、これは同じ駅だが別路線の駅アイコンが全く同じ場所に上書きされホバー時にその駅が感知されることが原因で、geojsonのproperties自体の情報が間違っている訳ではない)
- それ以外の時間はプレゼン資料準備に充てた、現在も引き続き資料作成中
