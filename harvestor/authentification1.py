
from tweepy import OAuthHandler


ACCESS_TOKEN = "1117988833436397568-vtgxrL2x0lhJvcPi8tKuRLntAKVqGB"
ACCESS_TOKEN_SECRET = "Uwioa9O9RNsA5JygK0bHX84UxsOKiMF283OQpeporN334"
CONSUMER_KEY = "IzabACqOqQ2XNshVSjA1lRWHp"
CONSUMER_SECRET = "rzVQDBOggdsO5NsKj6rzKYCRIMEI94t9Ka2XlkICNxg3gnt63i"


def getAuth(self):
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    return auth
