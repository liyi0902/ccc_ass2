
from tweepy import OAuthHandler

ACCESS_TOKEN = "988044719287549954-skN9LAPejtC5jePxe0yK5U0LXm89mRQ"
ACCESS_TOKEN_SECRET = "QTVWgbQUq0NKwW1UcQI0afX40coiyWr6a867lt7nBfjSK"
CONSUMER_KEY = "fxAkAR5lwg2Ruwp44iW4QlCdj"
CONSUMER_SECRET = "0g31TlRcU2LuwabCuziFRvPQvPIvkIOUe766wbUJqiSJjDhRQ8"


def getAuth(self):
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    return auth
