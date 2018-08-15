import requests
from bs4 import BeautifulSoup
import time
# chrome 打开网页后F12-network- 查找www.kugou.com 复制user-agent 两边要加单引号
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}

def get_info(url):
    web_data = requests.get(url,headers = headers)
    soup = BeautifulSoup(web_data.text,'lxml')
    ranks = soup.select('div.pc_temp_songlist > ul > li > span.pc_temp_num ')# #rankWrap > div.pc_temp_songlist > ul > li:nth-child(3) > span.pc_temp_num > strong   div.pc_temp_songlist > ul > li > span.pc_temp_num > strong
    titles = soup.select('div.pc_temp_songlist > ul > li > a') # 对歌手 - 歌名右键->检查->对弹出项COPY->SELECTOR 得到#rankWrap > div.pc_temp_songlist > ul > li:nth-child(1) > a 
    #可以确定'div.pc_temp_songlist > ul > li > a'
    times = soup.select('div.pc_temp_songlist > ul > li > span.pc_temp_tips_r > span') # #rankWrap > div.pc_temp_songlist > ul > li:nth-child(1) > span.pc_temp_tips_r > span 
    # 确定'div.pc_temp_songlist > ul > li > span.pc_temp_tips_r > span',教程上简写为span.pc_temp_tips_r > span，“由于某些标签是固定的，因此选用部分路径即可
    for rank,title,time in zip(ranks,titles,times):
        data = {
            '排位':rank.get_text().strip(),
            '歌手':title.get_text().split(' -')[0],# 信息结构为 歌手 - 歌名，分片' -'把歌手后的空格去掉
            '歌名':title.get_text().split('- ')[1],# 把'- '歌名前的空格去掉，取分片的第二部分
            '时长':time.get_text().strip()
        }
        print(data)
if __name__ == '__main__':
    urls = ['http://www.kugou.com/yy/rank/home/{}-8888.html'.format(str(i))for i in range(1,24)] # 1到23页 每页22个 format 并将i转为字符串类型
    for url in urls:
        get_info(url)
        time.sleep(1)# 每一次爬取停止一秒