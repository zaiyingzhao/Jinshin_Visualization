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
また特定キーワードを含むツイート数を取得するにはacademic research accessが必要らしいがこれは一般学生には付与されない模様**  

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
