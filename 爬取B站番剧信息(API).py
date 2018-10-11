import time
import requests
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}
url = 'https://bangumi.bilibili.com/api/timeline_v2_global'
time.sleep(1)
r = requests.get(url, headers=headers)
r_dict = r.json()

print(r_dict.keys())
for i in range(10):
    # //*[@id="app"]/div[1]/div[2]/div/div[2]/div[4]/span/text()
    print(r_dict['result'][i]['title'] + 
        '\n地区：', r_dict['result'][i]['area'] ,
        '\n追番数：', r_dict['result'][i]['attention'] ,
        '\n弹幕数：', r_dict['result'][i]['danmaku_count'] ,
        '\n播放量：', r_dict['result'][i]['play_count'] ,
        '\n更新时间：每周', r_dict['result'][i]['weekday'] ,
        '\n最近更新时间：', r_dict['result'][i]['lastupdate_at'] ,
         '\n\n'
         )

detail_url = "https://bangumi.bilibili.com/anime/{}"


