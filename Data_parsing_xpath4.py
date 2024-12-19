'''

- 项目需求：解析出所有城市名称https://www.aqistudy.cn/historydata/
'''
import requests
from lxml import etree
import os

if __name__ == '__main__':
    if not os.path.exists('./jainliLibs'):
        os.mkdir('./jainliLibs')

    url = 'http://sc.chinaz.com/jianli/free.html'
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
    # 拿到每一模板对应的链接
    a_list_url = tree.xpath('//div[contains(@class,"main_list")]/div/a/@href')
    for href_url in a_list_url:
        detail_text = requests.get(url=href_url, headers=headers).text
        tree = etree.HTML(detail_text)
        # 拿到下载链接
        down_url = tree.xpath('//div[contains(@class,"downlist")]/ul/li[1]/a/@href')[0]
        down_name = down_url.split('/')[-1]
        # print(down_url)
        # 下载模板
        down_content = requests.get(url=down_url, headers=headers).content
        with open('./jainliLibs/' + down_name, 'wb') as f:
            f.write(down_content)
            print(down_name, 'success!')

