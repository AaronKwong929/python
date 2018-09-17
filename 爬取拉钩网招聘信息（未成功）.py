import requests
import json
import time
headers = {
    'Cookie':
    'LGUID=20170318090857-76585811-0b77-11e7-94fa-5254005c3644; user_trace_token=20170318090856-17f9ec1cafce47be9f9d2448700ed0fd; index_location_city=%E5%85%A8%E5%9B%BD; PRE_UTM=m_cf_cpt_baidu_pc; PRE_HOST=bzclk.baidu.com; PRE_SITE=http%3A%2F%2Fbzclk.baidu.com%2Fadrc.php%3Ft%3D06KL00c00fATEwT0VZ9m0FNkUsaFl8Fm000000fS_W300000Txxy_Y.THL0oUhY1x60UWdBmy-bIfK15yw-rynvuWRknj0srj0kmWn0IHYLrHn4rDD4rHc1njnvwDRswR7DPH7jrH-Kwj6LnYNKwfK95gTqFhdWpyfqnWbzP1DsPWn3nBusThqbpyfqnHm0uHdCIZwsT1CEQLILIz4_myIEIi4WUvYEUZ0EpZwVUaqWUvdVUv38pZwVUjqdIAdxTvqdThP-5ydxmvuxmLKYgvF9pywdgLKW0APzm1Y1Pjb4Pf%26tpl%3Dtpl_10085_14394_1%26l%3D1051868676%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E3%252580%252590%2525E6%25258B%252589%2525E5%25258B%2525BE%2525E7%2525BD%252591%2525E3%252580%252591%2525E5%2525AE%252598%2525E7%2525BD%252591-%2525E4%2525B8%252593%2525E6%2525B3%2525A8%2525E4%2525BA%252592%2525E8%252581%252594%2525E7%2525BD%252591%2525E8%252581%25258C%2525E4%2525B8%2',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Connection':
    'keep-alive'
}


def get_page(url, params):
    # html = requests.get(url, data=params, headers=headers)
    page_number = 10
    get_info(url, page_number)


def get_info(url, page):
    for pn in range(1, page + 1):
        params = {'first': 'true', 'pn': str(pn), 'kd': 'python'}
        try:
            html = requests.post(url, data=params, headers=headers)
            json_data = json.loads(html.text)
            results = json_data['content']['positionResult']['result']
            for result in results:
                '''businessZones: result['businessZones']
                city: result['city']
                companyFullName: result['companyFullName']
                companyLabelList: result['companyLabelList']
                companySize: result['companySize']
                district: result['district']
                education: result['education']
                jobNature: result['jobNature']
                positionAdvantage: result['positionAdvantage']
                salary: result['salary']'''
                print(result['businessZones'])
                time.sleep(2)
        except IOError:
            pass


if __name__ == '__main__':
    url = 'https://www.lagou.com/jobs/positionAjax.json'
    params = {'first': 'true', 'pn': '1', 'kd': 'Python'}
    get_page(url, params)
