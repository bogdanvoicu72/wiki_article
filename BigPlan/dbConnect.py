import pymongo
import qrtools
from bson import ObjectId
from   pyzbar.pyzbar import decode
from PIL import Image
db_name  = 'test'
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client[db_name]

collection = 'products'
query_collection = db[collection]

d=  decode(Image.open('/Users/bogdanvoicu/PycharmProjects/BigPlan/media/image/TEST.png'))
print(d[0].data.decode('ascii'))