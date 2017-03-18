import mongoengine

host = "ds123370.mlab.com"
port = 23370
db_name = "khanhphamdinh"
username = "admin"
password = "admin"

def connect():
    mongoengine.connect(db= db_name, host = host,port = port,username = username,password = password)

def listjson(l):
    import json
    return [json.loads(item.to_json()) for item in l]

def itemjson(item):
    import json
    return json.loads(item.to_json())
