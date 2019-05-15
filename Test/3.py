import couchdb
import socket
import time
import json


class WebDb:

    def __init__(self):
        remoteIP = socket.gethostbyname(socket.gethostname())
        mycouchdb = couchdb.Server("http://172.26.38.193:5984")
        notConnected = True
        db_name = "tweets"
        while(notConnected):
            try:
                db = mycouchdb[db_name]
                self.db = db
                notConnected = False
            except:
                print("Server not Found,trying again in 10s")
                time.sleep(10)
                continue


if __name__ == '__main__':
    webDb = WebDb()
    ch = webDb.db.changes(feed='continuous', include_docs=True)
    counter = 0
    for each in ch:
        counter += 1
        if (counter > 1):
            print(each["doc"])
            counter = 0
