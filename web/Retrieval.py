import couchdb
import socket
import time
import json

import os


class WebDb:

    def __init__(self):
        project_Path = "/home/ubuntu/web"
        with open(project_Path+'/remoteDB.config', "r") as f:
            db_url = f.readline().strip()
            db_tweets_name = f.readline().strip()

        # db_url = "http://10.12.74.154:5984"
        mycouchdb = couchdb.Server(db_url)
        notConnected = True
        while(notConnected):
            try:
                db = mycouchdb[db_tweets_name]
                self.db = db
                notConnected = False
            except:
                print("Server not Found,trying again in 10s")
                time.sleep(10)
                continue


if __name__ == '__main__':
    webDb = WebDb()
    while True:
        ch = webDb.db.changes(feed='continuous', include_docs=True)
        counter = 0
        for each in ch:
            counter += 1
            if (counter > 1):
                print(each["doc"])
                counter = 0
