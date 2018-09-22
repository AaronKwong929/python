import time
import requests
# 难点在于找api
# 打开详细视频页面 F12 - network - F5 - XHR - response - 找需要的内容 
# 获取到api网址https://api.bilibili.com/x/web-interface/view?aid=32127626 验证之
# 接下来的都是json获取操作
url = 'https://api.bilibili.com/x/web-interface/archive/stat?aid=32127626'
time.sleep(2)
r = requests.get(url)
response_dict = r.json()
print('播放量：', response_dict['data']['view'], '  弹幕数：',
      response_dict['data']['danmaku'], 
      '  推荐数：', response_dict['data']['like'],
      '  评论数：', response_dict['data']['reply'], 
      '  投币数：', response_dict['data']['coin'], 
      '  收藏数：', response_dict['data']['favorite'], 
      '  分享数：', response_dict['data']['share'])
