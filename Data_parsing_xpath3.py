'''

- 项目需求：解析出所有城市名称https://www.aqistudy.cn/historydata/
'''
import requests
from lxml import etree
import os

if __name__ == '__main__':

    url = 'https://www.aqistudy.cn/historydata/'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    # 爬取页面源码数据
    response = requests.get(url=url, headers=headers)
    # 可以手动把响应数据编码成utf-8
    # response.encoding='GBK'
    page_text = response.text
    # 数据解析
    tree = etree.HTML(page_text)

    li_list = tree.xpath('//div[@class="bottom"]//li')
    for li in li_list:
        city_name = li.xpath('./a/text()')[0]
        print(city_name)

