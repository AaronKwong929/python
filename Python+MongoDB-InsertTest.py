import pymongo

client = pymongo.MongoClient('localhost', 27017)
mydb = client['mydb']
musictop = mydb['musictop']

info1 = {
    'name': 'Best Friend',
    'author': 'Sofi Tukker, NERVO, The Knocks, Alisa Ueno',
    'style': '流行',
    'publishTime': '2017-09-12',
    'publisher': '未知',
    'score': '9.5'
}

# musictop.insert_one(info1)  # 插入一条
info2 = {
    'name': 'COSMIC',
    'author': 'Bazzi',
    'style': '流行',
    'publishTime': '2018-04-12',
    'publisher': '未知',
    'score': '9.6'
}

musictop.insert_many([info1, info2])  # 插入多条
