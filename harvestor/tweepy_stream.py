from tweepy.streaming import StreamListener
from tweepy import Stream
import authentification1
import authentification2
import authentification3
import authentification4
import authentification5
import json
import insights

# # # # TWITTER STREAMER # # # #


class TwitterStreamer():

    def __init__(self):
        pass

    def stream_tweets(self, listener, parameter):
        Vic_BOUND_BOX = (140.9617, -39.1592, 149.9763, -33.9806)
        # Vic_BOUND_BOX = (0, 10, 120, 80)
        if parameter == "1":
            auth = authentification1.getAuth(self)
        elif parameter == "2":
            auth = authentification2.getAuth(self)
        elif parameter == "3":
            auth = authentification3.getAuth(self)
        elif parameter == "4":
            auth = authentification4.getAuth(self)
        elif parameter == "5":
            auth = authentification5.getAuth(self)
        stream = Stream(auth, listener)
        stream.filter(locations=Vic_BOUND_BOX, languages=["en"])


class StdOutListener(StreamListener):

    def __init__(self, db):
        self.db = db

    def getText(self, data):
        try:
            text = data['quoted_status']['extended_tweet']['full_text']
        except:
            try:
                text = data['quoted_status']['full_text']
            except:
                try:
                    text = data['extended_tweet']['full_text']
                except:
                    try:
                        text = data['full_text']
                    except:
                        try:
                            text = data['text']
                        except:
                            text = ""
        return text

    def getHashTags(self, data):
        try:
            hashtags = data["quoted_status"]["extended_tweet"]["entities"]["hashtags"][0]["text"]
        except:
            try:
                hashtags = data["quoted_status"]["entities"]["hashtags"][0]["text"]
            except:
                try:
                    hashtags = data["extended_tweet"]["entities"]["hashtags"][0]["text"]
                except:
                    try:
                        hashtags = data["entities"]["hashtags"][0]["text"]
                    except:
                        try:
                            hashtags = data["entities"]["hashtags"][0]["text"]
                        except:
                            hashtags = []
        return hashtags

    def on_data(self, row_data):
        try:
            dic = {}
            data = json.loads(row_data)
            if data["coordinates"] is not None:
                if data["id_str"] not in self.db:
                    dic["friends_count"] = str(data["user"]["friends_count"])
                    dic["coordinates"] = data["coordinates"]["coordinates"]
                    dic["username"] = data["user"]["name"].encode('ascii', 'ignore')
                    dic["text"] = self.getText(data).encode('ascii', 'ignore')
                    dic["hashtags"] = self.getHashTags(data)
                    dic["suburb"] = insights.get_location(data["coordinates"]["coordinates"])
                    dic["gender"] = insights.get_gen(dic["username"])
                    dic["anger"] = insights.is_angry(dic["text"])
                    line = str(dic)+"\n"
                    self.db[data["id_str"]] = dic
                    print(line)
            return True
        except Exception as e:
            print(str(e))

    def on_error(self, status_code):
        if status_code == 420:
            print("the request is frequent!!!please try  using other authentification")
