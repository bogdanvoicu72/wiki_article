from hashlib import sha256
from time import gmtime, strftime
from datetime import datetime
import json
import pymongo
from bson.objectid import ObjectId
import pyqrcode
import png
from pyqrcode import QRCode


class Block():
    def __init__(self, Model, Brand, Time, Index, tip_produs, previous_hash):
        self.Model = Model
        self.Brand = Brand
        self.Time = Time
        self.Index = Index
        self.tip_produs = tip_produs
        self.previous_hash = previous_hash
        self.hash = sha256(self.to_string().encode()).hexdigest()

    def is_hash_valid(self, hash):
        return (hash.startswith('0' * 3))

    def calculate_valid_hash(self):
        hash = ''
        nonce = 0
        while (not self.is_hash_valid(hash)):
            temp = self.to_string() + str(nonce)
            hash = sha256(temp.encode()).hexdigest()
            nonce += 1
        self.hash

    def to_string(self):
        return "{0}\t{1}\t{2}\t{3}\t{4}\t{5}".format(self.Model, self.Brand, self.Time, self.Index, self.tip_produs,
                                                     self.previous_hash)

    def dict_for_json(self):
        d = {}
        d["model"] = self.Model
        d["brand"] = self.Brand
        d["tip_produs"] = self.tip_produs
        d["Time Creation"] = self.Time
        d["Index"] = self.Index
        d["Previous_Hash"] = self.previous_hash
        return d

    def get_hash(self):
        return self.hash

    def get_prev_hash(self):
        return self.previous_hash


class Blockchain():
    def __init__(self):
        self.blocks = []
        self.set_genesis_block()

    def set_genesis_block(self):
        Model = "First t-shirt Summer 2020"
        Brand = "Nike"
        Date_Time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        Index = 0
        tip_produs = "tricou"
        prev_hash = '0' * 64
        genesis_block = Block(Model, Brand, Date_Time, Index, tip_produs, prev_hash)
        self.blocks.append(genesis_block)

    def get_last_hash(self):
        last_block = self.blocks[-1]
        last_hash = last_block.hash
        return (last_hash)

    def add_new_block(self, Model, Brand, Date_Time, Index, tip_produs):
        prev_hash = self.get_last_hash()
        new_block = Block(Model, Brand, Date_Time, Index, tip_produs, prev_hash)
        self.blocks.append(new_block)

    def get_blocks(self):
        return (self.blocks)
    # def get_current_hash(self):
    #  for k in blocks:


bl = Blockchain()
bl.add_new_block("Summer 2020 Green color", "Nike", datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 1, "tricou")
bl.add_new_block("Summer 2020 Green color", "Nike", datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 2, "tricou")
bl.add_new_block("Summer 2020 Green color", "Nike", datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 3, "tricou")
bl.add_new_block("Summer 2020 Green color", "Nike", datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 3, "parfum")
#    for block in bl.get_blocks():
#        print(block.to_string())
products_dict = {}
products = bl.get_blocks()
for product in products:
    if product.tip_produs not in products_dict:
        products_dict[product.tip_produs] = []
        products_dict[product.tip_produs].append(product.dict_for_json())
    else:
        products_dict[product.tip_produs].append(product.dict_for_json())
# json_object = json.dumps(products_dict, indent=4) #entire json structure with products
for key, value in products_dict.items():
    new_str_dict = {}
    new_str_dict[key] = value
    json_object = json.dumps(new_str_dict, indent=4)
    print(json_object)
    with open(str(key) + ".json", "w") as file:
        file.write(json_object)

# for i in bl.blocks:
#   print(bl.blocks[0].get_hash())
# print(i.get_hash())


#db_name = 'product'
#test_client = pymongo.MongoClient('mongodb://localhost:27017/')
#test_db = test_client[db_name]

#collection = 'products'
#test_collection = test_db[collection]

#with open('tricou.json', 'r') as json_data:
 #   dict_json = json.load(json_data)

# id-ul fiecarui obiect
# document = test_collection.find_one({'_id': ObjectId(post_id)})
# print(document)

#post_id = test_collection.insert_one(dict_json).inserted_id
#print(post_id)
###search in database for ObjectID and Previous_Hash
#qu = test_collection.find_one({'_id': ObjectId(post_id)}, {'Previous_Hash': bl.blocks[1].get_hash()})
#print(qu)

#qu2 = test_collection.find_one(
#    "tricou.Previous_Hash":'0000000000000000000000000000000000000000000000000000000000000000')

#print(qu2)


def get_object_hash():
    #i = int(input("What hash do you want?:"))
    prev_test = '79f6e19a615b75c16dcb1f0fdd556be31cc971e6f625173ecef77e92fab8bbee'
    id_test ='5f24595ed07d45f2ea5e48a7'
    #str1 = str(bl.blocks[i-1].get_hash())
    conca = str(id_test) + 'and' + str(prev_test)
   # print (str1)
    print (conca)
get_object_hash()
prev_test = '79f6e19a615b75c16dcb1f0fdd556be31cc971e6f625173ecef77e92fab8bbee'

def split_fucntion(code):
    what_split =  code
    split = what_split.split("and")
    argument1 = split[0]
    argument2 = split[1]
    #print(argument1)
    #print(argument2)
   # q = test_collection.find_one(

      #  {'_id': ObjectId(str(argument1))}, {'tricou': {
       #     '$elemMatch': {'Previous_Hash': str(argument2)
#
 #                          }
  #      }}

   # )
   # print(q)

split_fucntion('5f2e80bf779c4603a8b1bc2aand4fb494fd186cb139a638c13cf30c48f2cddb78ad6d731333c529dbd9f25c56e7')

#test_client.close()

# The web framework gets post_id from the URL and passes it as a string
# def get(post_id):
# Convert from string to ObjectId:
#   document = client.db.collection.find_one({'_id': ObjectId(post_id)})