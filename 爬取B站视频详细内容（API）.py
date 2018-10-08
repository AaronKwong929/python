import time
import requests
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}
# 难点在于找api
# 打开详细视频页面 F12 - network - F5 - XHR - response - 找需要的内容 
# 获取到api网址https://api.bilibili.com/x/web-interface/view?aid=32127626 验证之
# ps:b站视频信息的api地址都为：https://api.bilibili.com/x/web-interface/archive/stat?aid=  后面为av号数字
# 接下来的都是json获取操作
av = input('请输入视频AV号后的数字：')
url = 'https://api.bilibili.com/x/web-interface/archive/stat?aid={}'.format(str(av))
time.sleep(2)
r = requests.get(url, headers=headers)
response_dict = r.json()
print('视频av号：' + 'av' + str(av),
      '  播放量：', response_dict['data']['view'], 
      '  弹幕数：', response_dict['data']['danmaku'], 
      '  推荐数：', response_dict['data']['like'],
      '  评论数：', response_dict['data']['reply'], 
      '  投币数：', response_dict['data']['coin'], 
      '  收藏数：', response_dict['data']['favorite'], 
      '  分享数：', response_dict['data']['share'])