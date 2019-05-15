import couchdb
import os
if __name__ == '__main__':
    with open('/home/ubuntu/dbServer/localDB.config', "r") as f:
        db_url = f.readline().strip()
        db_tweets_name = f.readline().strip()
    mycouchdb = couchdb.Server(db_url)
    try:
        db = mycouchdb.create(db_tweets_name)
    except couchdb.http.PreconditionFailed:
        db = mycouchdb[db_tweets_name]
