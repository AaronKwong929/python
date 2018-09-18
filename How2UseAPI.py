import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=start'

r = requests.get(url)  # 返回请求状态

print('status_code:', r.status_code)
response_dict = r.json()
print(response_dict.keys())  # 返回api内的关键字
print('\ntotal repositories:', response_dict['total_count'])  # 返回total_count关键字内容
repo_dicts = response_dict['items']
print('repositories_return:', len(repo_dicts))  # 返回字典长度
repo_dict = repo_dicts[0]  # 取字典内第一项
print('repo_id:' + str(repo_dict['id']))  # 打印其中内容
print('repo_name:' + repo_dict['name'])
print(repo_dict['owner']['login'])  # 字典内嵌字典获取内容方式