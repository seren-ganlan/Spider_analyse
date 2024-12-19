'''
from lxml import etree
1.将本地的html文档中的源码数据加载到etree对象中
   tree=etree.parse(filePath)
2.可以将互联网上获取的源码数据加载到该对象中
   etree.HTML('page_text')

属性定位：
    #找到class属性值为song的div标签
    //div[@class="song"]
层级&索引定位：
    - xpath('xpath表达式') 根据层级关系进行标签定位
        tree.xpath('/html/body/div')
        tree.xpath('/html//div')
        tree.xpath('//div') 匹配所有div
        /: 表示的是从跟节点开始定位，表示的是一个层级
        //:表示的是多个层级 (不只是2个),相当于找所有
    #找到class属性值为tang的div的直系子标签ul下的第二个子标签li下的直系子标签a
    //div[@class="tang"]/ul/li[2]/a
逻辑运算：
    #找到href属性值为空且class属性值为du的a标签
    //a[@href="" and @class="du"]
模糊匹配：
    //div[contains(@class, "ng")]
    //div[starts-with(@class, "ta")]
取文本：
    # /表示获取某个标签下的文本内容
    # //表示获取某个标签下的文本内容和所有子标签下的文本内容
    //div[@class="song"]/p[1]/text()
    //div[@class="tang"]//text()
取属性：
    //div[@class="tang"]//li[2]/a/@href
'''

import requests
from lxml import etree

if __name__ == '__main__':

    url = 'https://bj.58.com/ershoufang/'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    # 爬取页面源码数据
    page_text = requests.get(url=url, headers=headers).text
    # 数据解析
    tree = etree.HTML(page_text)
    # 观察源码 拿到li列表
    li_list = tree.xpath('//ul[@class="house-list-wrap"]/li')
    for li in li_list:
        title = li.xpath('./div[2]/h2[@class="title"]/a//text()')[0]  # ./ 表示li标签的位置
        price = li.xpath('./div[3]/p[@class="sum"]//text()')[0] + li.xpath('./div[3]/p[@class="sum"]//text()')[
            1]  # ./ 表示li标签的位置

        print(title, price)