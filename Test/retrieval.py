import couchdb
import socket

db_name = "yhq"


class WebDb:
    def __init__(self):
        remoteIP = socket.gethostbyname(socket.gethostname())
        mycouchdb = couchdb.Server("http://"+remoteIP+":5984")
        db_name = "yhq"
        notConnected = True
        while(notConnected):
            try:
                db = mycouchdb[db_name]
                self.db = db
                notConnected = False
            except couchdb.http.PreconditionFailed:
                continue


webDb = WebDb()
ch = webDb.db.changes(feed='continuous', include_docs=True)
counter = 0
for each in ch:
    counter += 1
    if (counter > 1):
        print(each["doc"])
        counter = 0
# for row in db.query(map_fun, descending=True):
#     print(row.key)
# print(row.value)
# for ele in db[id_str]:
#     print(ele["count"])
#     print(ele["text"])
# data["item"] = doc.value
# print(data["item"], type(data["item"]))
