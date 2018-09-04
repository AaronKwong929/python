import csv
f = open('C://Users/Arron/Desktop/csvtest.csv', 'w+')
writer = csv.writer(f)
writer.writerow(('id', 'name'))
writer.writerow(('1', 'li'))
writer.writerow(('2', 'wong'))