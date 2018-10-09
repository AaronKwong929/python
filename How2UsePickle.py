import pickle

dict_1 = {'a': 123, 'b': 456, 'c':{'d': 789, 'e':'abcd'}}
file = open('pickle_example.pickle', 'wb')
pickle.dump(dict_1, file)  # 将dict_1 添加到file中
file.close()

file= open('pickle_example.pickle', 'rb')
dict_2 = pickle.load(file)  # 将file加载到dict_2中
file.close()
print(dict_2)