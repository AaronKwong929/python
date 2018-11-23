import re
import requests

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}

f = open('C://Users/Arron/Desktop/dp.txt', 'a+')


def get_info(url):
    res = requests.get(url, headers=headers)
    if res.status_code != 404:
        contents = re.findall('<p>(.*?)</p>', res.content.decode('utf-8'),
                              re.S)
        for content in contents:
            f.write(content + '\n')
    else:
        pass


if __name__ == '__main__':
    urls = [
        'http://www.doupoxs.com/doupocangqiong/{}.html'.format(str(i))
        for i in range(2, 100)
    ]
    for url in urls:
        get_info(url)
    f.close()
