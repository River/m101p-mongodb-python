import bottle
import pymongo

@bottle.route('/')
def index():
    connection = pymongo.MongoClient('localhost', 27017)
    db = connection.test
    name = db.names
    item = name.find_one()

    return 'Hello %s!' % item['name']

bottle.run(host='localhost', port=8000)
