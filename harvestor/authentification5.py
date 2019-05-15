
from tweepy import OAuthHandler


CONSUMER_KEY = 'qf2EtIgAGdPdbUvzBOTqk832q'
CONSUMER_SECRET = 'gWhdWIE1aaD1SmaCOxMM0qiCxcFuRoljr98yi6JxliF6lF9mHN'
ACCESS_TOKEN = '1121040463337639936-PTrHl0c9FYjT1GilT548v6fEHpGc8v'
ACCESS_TOKEN_SECRET = 'oStwqtPcKLQRaULgaI2jelNJxiZ5BlKWyC975mvaxGSGt'


def getAuth(self):
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    return auth
