import couchdb
from tweepy_stream import TwitterStreamer, StdOutListener
import sys
if __name__ == '__main__':
    with open('/home/ubuntu/harvestor/remoteDB.config', "r") as f:
        db_url = f.readline().strip()
        db_tweets_name = f.readline().strip()
    mycouchdb = couchdb.Server(db_url)
    RemoteCouchdb = couchdb.Server(db_url)
    parameter = sys.argv[1]
    notConnected = True
    while notConnected:
        try:
            tweets_db = RemoteCouchdb[db_tweets_name]
            notConnected = False
        except Exception as e:
            print(str(e))
            # print("not found,will try again in 10s")
            # time.sleep(10)
            continue
    twitter_streamer = TwitterStreamer()
    listener = StdOutListener(tweets_db)
    print(parameter)
    twitter_streamer.stream_tweets(listener, parameter)
