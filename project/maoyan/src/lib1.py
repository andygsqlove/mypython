import requests
import sys
from myheader import headers
import re


class Maoyan:
    '''
    This class all method is static.And its function is to get the source
    code from manyan top 100(http://maoyan.com/board/4)
    and parse the source code and get the data.
    '''
    @staticmethod
    def get_onepage(url):
        try:
            response = requests.get(url,headers = headers)
        except requests.exceptions.ConnectionError as econ:
            print('connectionError !')
            sys.exit(1)
        except:
            print('happend undefind error!')
            sys.exit(2)
        if response.status_code == 200:
            print('get url successed!')
            #response.encoding = 'utf-8'
            return response.text

    @staticmethod
    def parse_one_page(html):
        parttern = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?'
                             '<p.*?class="name">.*?>(.*?)</a>.*?'
                             '<p.*?class="star">(.*?)</p>.*?'
                             '<p.*?class="releasetime".*?>(.*?)</p>.*?'
                             '<p.*?class="score">.*?integer.*?>(.*?)</i>.*?'
                             'fraction.*?>(.*?)</i>',re.S)
        items = re.findall(parttern,html)
        for item in items:
            yield {
                'id':item[0].strip(),
                'name':item[1].strip(),
                'star':item[2].strip()[3:],
                'releasetime':item[3].strip()[5:],
                'score':item[4].strip() + item[5].strip()
            }
            # print(item[0])
            # print(item[1])
            # print(item[2])
            # print(item[3])
            # print(item[4])
            # print(item[5])

def test_lib1():
    base_url = 'http://maoyan.com/board/4?offset='
    for i in range(0,100,10):
        url = base_url + str(i)
        html = Maoyan.get_onepage(url)
        datas = Maoyan.parse_one_page(html)
        for data in datas:
            print(data)
