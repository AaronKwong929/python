import pymongo

client = pymongo.MongoClient('localhost', 27017)
mydb = client['mydb']
musictop = mydb['musictop']

results = musictop.find()

for result in results:
    print(result)