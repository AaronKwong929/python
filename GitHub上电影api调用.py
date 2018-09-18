import requests

url = 'https://api-m.mtime.cn/PageSubArea/HotPlayMovies.api?locationId=290'
r = requests.get(url)
print(r.status_code)
response_dict = r.json()
print(response_dict.keys())
movie_dicts = response_dict['movies']
for movie_dict in movie_dicts:
    print('电影名：' + movie_dict['titleCn'] + '(' + movie_dict['titleEn'] + ')')
    print('主演1：' + movie_dict['actorName1'])
    print('主演2：' + movie_dict['actorName2'])
    print('导演：' + movie_dict['directorName'])
    print('简介：' + movie_dict['commonSpecial'])
    print('类型：' + movie_dict['type'])
    print('\n')
