import pymongo

client = pymongo.MongoClient('localhost', 27017)
mydb = client['mydb']
musictop = mydb['musictop']

# musictop.remove()  # 删除全部内容

musictop.delete_one({'name': 'Mine'})  # 删除指定单一内容（第一条数据）
# musictop.delete_many({'name': {'$lt': 'COSMIC'}})  # 删除所有符合条件的内容
# 参考http://developer.51cto.com/art/201805/573924.htm
