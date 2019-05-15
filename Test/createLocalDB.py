import couchdb

mycouchdb = couchdb.Server("http://localhost:5984")
db_name = "yhq"
try:
    db = mycouchdb.create(db_name)
except couchdb.http.PreconditionFailed:
    db = mycouchdb[db_name]
