
from tweepy import OAuthHandler

ACCESS_TOKEN = "981533044522627072-YFGoc8FBwK6pqOXc5teJhFnPcu3ghtg"
ACCESS_TOKEN_SECRET = "yXc72kyxq8F5EqtDacD1Kdneddm1XnfS1u57uS3tVyBmx"
CONSUMER_KEY = "c67rYQVxBfyQAqrN9oMes59PB"
CONSUMER_SECRET = "ougb9ujqYgT1AJ1VtcsjVvpjfKTkqj0IljTrcgZBTp4kgbDw4M"


def getAuth(self):
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    return auth
