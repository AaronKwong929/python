import requests
import time
# import math  # 方法1
'''
# 方法1
url = 'https://space.bilibili.com/ajax/member/getSubmitVideos?mid=122879&page=1'  # 先解析一次网页 获取视频总数
r = requests.get(url)
dict = r.json()
page = math.ceil(dict['data']['count'] / 20) + 1  # range(int) +1
urls = ['https://space.bilibili.com/ajax/member/getSubmitVideos?mid=122879&page={}'.format(str(i))for i in range(page)]
'''
# 方法2
urls = ['https://space.bilibili.com/ajax/member/getSubmitVideos?mid=122879&page={}'.format(str(i))for i in range(15)]  # 15是手工观察厂长视频数（266）个 266/20 = 13.3 向上取整 + 1（range()）得出  # pss:B站ajax的json内容是20个视频内容为一页
for url in urls:
    r = requests.get(url)
    dict = r.json()
    for m in range(20):
        try:
            print(
                '视频名：' + dict['data']['vlist'][m]['title'],
                '  视频号：' + 'av' + str(dict['data']['vlist'][m]['mid']),
                '  播放量：' + str(dict['data']['vlist'][m]['play']),
                '  评论数：' + str(dict['data']['vlist'][m]['comment']),
                '  视频简介：' + str(dict['data']['vlist'][m]['description']),
                '  收藏数：' + str(dict['data']['vlist'][m]['favorites']),
                '  视频长度：' + dict['data']['vlist'][m]['length']
            )
            print()
        except IndexError:
            pass  # 最后一页内容不足20个，pass掉
    time.sleep(1)