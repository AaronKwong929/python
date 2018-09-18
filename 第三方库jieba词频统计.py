import jieba.analyse
path = 'C:/Users/Arron/Desktop/dp.txt'
f = open(path, 'r')
content = f.read()
try:
    jieba.analyse.set_stop_words('中文停用词表.txt')
    tags = jieba.analyse.extract_tags(content, topK=100, withWeight=True)
    for item in tags:
        print(item[0] + '\t' + str(int(item[1]*1000)))
except IOError:
    pass
