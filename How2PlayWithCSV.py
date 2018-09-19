import csv
f = open('C://Users/Arron/Desktop/doubantop250.csv', 'r', encoding='utf-8')  # 读取csv文件，'r'读模式
reader = csv.DictReader(f)
for row in reader:  # 打印文件内容
    print(row)
book1 = [
    'test1', 'https://test1.com/1234567/', '张三', 'testpublish', '1970-1',
    ' 0.00元', '10.0', 'test'
]
out = open('C://Users/Arron/Desktop/doubantop250.csv', 'a', newline='', encoding='utf-8')  # 'a'末尾追加，无则创建
writer = csv.writer(out, dialect='excel')
writer.writerow(book1)
f.close()
