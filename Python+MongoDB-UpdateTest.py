import pymongo

client = pymongo.MongoClient('localhost', 27017)
mydb = client['mydb']
musictop = mydb['musictop']

condition = {'name': 'COSMIC1'}
info = musictop.find_one(condition)
info['name'] = 'COSMIC'
musictop.update_one(condition, {'$set': info})
# result = musictop.update(condition, info)
# print(info)
#  参考http://developer.51cto.com/art/201805/573924.htm