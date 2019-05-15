import couchdb
from tweepy_stream import TwitterStreamer, StdOutListener
import time
if __name__ == '__main__':
    db_tweets_name = "tweets"
    # db_users_name = "users"
    db_url = "http://172.26.38.193:5984"
    RemoteCouchdb = couchdb.Server(db_url)
    notConnected = True
    while notConnected:
        try:
            tweets_db = RemoteCouchdb[db_tweets_name]
            notConnected = False
        except:
            print("not found,will try again in 10s")
            time.sleep(10)
            continue
    twitter_streamer = TwitterStreamer()
    listener = StdOutListener(tweets_db)
    twitter_streamer.stream_tweets(listener)
