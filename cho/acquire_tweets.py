import tweepy

# 取得したキーを入力
API_KEY = ''
API_KEY_SECRET = ''
BEARER_TOKEN = ''
ACCESS_TOKEN = ''
ACCSESS_TOKEN_SECRET = ''

#リファレンスの内容に沿って入力（https://docs.tweepy.org/en/stable/client.html）
client = tweepy.Client(bearer_token = BEARER_TOKEN, consumer_key = API_KEY, consumer_secret = API_KEY_SECRET, access_token = ACCESS_TOKEN, access_token_secret = ACCSESS_TOKEN_SECRET)

# 検索ワード
QUERY = "京王線"
# Tweetを取得する上限
MAX_RESULTS = 10

# search_recent_tweetsは直近7日間のツイートしか取得できない
# search_all_tweetsはacademic accessが付与されていないと使えない (https://qiita.com/TakeshiNickOsanai/items/cf695370dde1ec21dbd6)
tweets = client.search_recent_tweets(query=QUERY, max_results=MAX_RESULTS, start_time="2022-11-01T00:00:00Z", end_time="2022-11-01T23:59:59Z")

tweets_data = tweets.data

if tweets_data != None:
    for i, tweet in enumerate(tweets_data):
        print("No:" + str(i+1))
        print("tweet.text: " + tweet.text)
        print("\n")
else:
    print("該当なし")