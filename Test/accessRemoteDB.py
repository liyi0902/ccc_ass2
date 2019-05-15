import couchdb
import socket
import  time

class CouchBase:

    def __init__(self):
        remoteIP = socket.gethostbyname(socket.gethostname())
        mycouchdb = couchdb.Server("http://"+remoteIP+":5984")
        db_name = "yhq"
        isNotConnected = True
        while isNotConnected:
            try:
                db = mycouchdb[db_name]
                self.db = db
                isNotConnected = False
            except couchdb.http.PreconditionFailed:
                continue


if __name__ == '__main__':
    id = 0
    count = 0
    Couchdb = CouchBase()
    while True:
        id += 1
        count += 1
        id_str = str(id)
        if id_str not in Couchdb.db:
            Couchdb.db[id_str] = {"count": count, "text": id}
            time.sleep(5)
