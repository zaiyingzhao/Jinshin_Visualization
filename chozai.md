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
