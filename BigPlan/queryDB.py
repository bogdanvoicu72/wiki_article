import pymongo
from bson.objectid import ObjectId
import blockchain

db_name = 'test'
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client[db_name]


collection = 'products'
t_collection = db[collection]
object_id = '5f24595ed07d45f2ea5e48a7'

objectID = t_collection.find_one({'_id': ObjectId(object_id)})
print(objectID)

object_hash = '0000000000000000000000000000000000000000000000000000000000000000'
q = t_collection.find_one(

    {'_id': ObjectId(object_id)},{'tricou': {
        '$elemMatch':{'Previous_Hash':object_hash

        }
    }}



)

print(q)

#{"tricou.Previous_Hash": object_hash}, {"tricou.$": 1}


#i = int(input("Index of object: "))
#str1 = str(blockchain.bl.blocks[i-1].get_hash())
#print(str1)

#def concat_objectId_hash():
 #   string_concat = str(objectID)+ '_' + 'and' + '_' + str(object_hash)

  #  return (string_concat)