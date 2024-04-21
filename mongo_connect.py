import pymongo

print("In pymongo")

def mongo_connection(id, data):

    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    db = client['rabbitmq_data']
    collection = db['mySampleString']
    dictionary_data = {'id':id, 'data':data}
    collection.insert_one(dictionary_data)
