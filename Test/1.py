import couchdb
import urllib2
import json
dbName = 'tweets3'
ServerUrl = "http://127.0.0.1:5984/"
designName = 'suburbs'

server = couchdb.Server(ServerUrl)

db = server[dbName]

test_view = """function (doc) {
  emit(doc.suburb, 1);
}"""

design = {'views': {"sub_lst": {'map': test_view, 'reduce': '_count'}}, 'language': 'javascript'}

db["".join("_design/"+designName)] = design


url = ServerUrl+dbName+'/_design/'+designName+'/_view/sub_lst?reduce=true&group_level=1'

contents = urllib2.urlopen(url).read()

data = json.loads(content.decode("utf-8").replace("'", '"'))

print(data)
