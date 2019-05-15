#!/usr/bin/env python
# coding=utf-8
from flask import Flask, render_template, request, url_for
import json
import urllib
import couchdb

# Connecting to the database and creating views, if not available
db_name = 'melb'
server_url = "http://172.26.38.193:5984/"
design_name = 'test2'
server = couchdb.Server(server_url)
db = server[db_name]
view_name = "test"
test_view = """
    function (doc) {
        if(doc.suburb != null && doc.gender != null && doc.angry>=0){
            emit([doc.suburb,doc.gender,doc.angry], 1);
        }
    }
"""

red = """
    function(keys, values, rereduce) {
        return sum(values);
    }
"""

# Check if view exists, else make view
try:
    design = {'views': {view_name: {'map': test_view, 'reduce': red}}, 'language': 'javascript'}
    db["".join("_design/" + design_name)] = design
except Exception as e:
    print e

# Csv converted to json that has Alcohol and Crime Values
with open('web/info_melb.json') as f:
    location = json.load(f)


app = Flask(__name__)
app.config['SECRET_KEY'] = "dfdfdffdad"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/s1/')
def s1():
    # Get data from the server
    url = server_url + db_name + '/_design/' + design_name + \
        '/_view/' + view_name + '?reduce=true&group_level=1'
    data1 = urllib.urlopen(url).read()
    data = json.loads(data1.encode("ascii"))
    names = []
    value = []
    for i in range(0, len(data['rows'])):
        if data['rows'][i]['key'][0] is None:
            pass
        else:
            if str(data['rows'][i]['key'][0]) in location.keys():
                value.append(data['rows'][i]['value'])
                names.append(str(data['rows'][i]['key'][0]))

    # Normalizing values
    norm_v = [float(i) / sum(value) for i in value]
    return render_template('s1.html', names=names, data=norm_v)


@app.route('/s2/')
def s2():
    url = server_url + db_name + '/_design/' + design_name + \
        '/_view/' + view_name + '?reduce=true&group_level=3'
    data1 = urllib.urlopen(url).read()
    data = json.loads(data1.encode("ascii"))
    city = []
    female = []
    male = []
    flag = 0
    for i in range(0, len(data['rows'])):
        if i % 2 != 0:
            if str(data['rows'][i]['key'][0]) in location.keys():
                if flag == 2:
                    male.append(int(data['rows'][i]['value']))
                    flag = 0
                elif flag == 0:
                    city.append(str(data['rows'][i]['key'][0]))
                    female.append(int(data['rows'][i]['value']))
                    flag = 2

    norm_m = [float(i) / sum(male) for i in male]
    norm_f = [float(i) / sum(female) for i in female]

    return render_template('s2.html', city=city, female=norm_f, male=norm_m)


@app.route('/s3/')
def s3():
    url = server_url + db_name + '/_design/' + design_name + \
        '/_view/' + view_name + '?reduce=true&group_level=1'
    data1 = urllib.urlopen(url).read()
    data = json.loads(data1.encode("ascii"))
    names = []
    value = []
    for i in range(0, len(data['rows'])):
        if data['rows'][i]['key'][0] is None:
            pass
        else:
            if str(data['rows'][i]['key'][0]) in location.keys():
                value.append(data['rows'][i]['value'])
                names.append(str(data['rows'][i]['key'][0]))

    norm_v = [float(i) / sum(value) for i in value]
    adata = []
    for i in range(0, len(names)):
        adata.append(location[names[i]]['alcohol'])
    norm_a = [float(i) / sum(adata) for i in adata]

    return render_template('s3.html', names=names, data1=norm_v, data2=norm_a)


@app.route('/s4/')
def s4():
    url = server_url + db_name + '/_design/' + design_name + \
        '/_view/' + view_name + '?reduce=true&group_level=1'
    data1 = urllib.urlopen(url).read()
    data = json.loads(data1.encode("ascii"))
    names = []
    value = []
    for i in range(0, len(data['rows'])):
        if data['rows'][i]['key'][0] is None:
            pass
        else:
            if str(data['rows'][i]['key'][0]) in location.keys():
                value.append(data['rows'][i]['value'])
                names.append(str(data['rows'][i]['key'][0]))

    norm_v = [float(i) / sum(value) for i in value]
    cdata = []
    for i in range(0, len(names)):
        cdata.append(location[names[i]]['crime'])
    norm_c = [float(i) / sum(cdata) for i in cdata]

    return render_template('s4.html', names=names, data1=norm_v, data2=norm_c)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=9999)
