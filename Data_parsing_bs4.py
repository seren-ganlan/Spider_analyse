"""
使用流程：
    - 导包：from bs4 import BeautifulSoup
    - 使用方式：可以将一个html文档，转化为BeautifulSoup对象，然后通过对象的方法或者属性去查找指定的节点内容
        （1）转化本地文件：
             - soup = BeautifulSoup(open('本地文件'), 'lxml')
        （2）转化网络文件：
             - soup = BeautifulSoup('字符串类型或者字节类型', 'lxml')
        （3）打印soup对象显示内容为html文件中的内容
基础巩固：
    （1）根据标签名查找
        - soup.a   只能找到第一个符合要求的标签
    （2）获取属性
        - soup.a.attrs  获取a所有的属性和属性值，返回一个字典
        - soup.a.attrs['href']   获取href属性
        - soup.a['href']   也可简写为这种形式
    （3）获取内容
        - soup.a.string
        - soup.a.text
        - soup.a.get_text()
       【注意】如果标签还有标签，那么string获取到的结果为None，而其它两个，可以获取文本内容
    （4）find：找到第一个符合要求的标签
        - soup.find('a')  找到第一个符合要求的
        - soup.find('a', title="xxx")
        - soup.find('a', alt="xxx")
        - soup.find('a', class_="xxx")
        - soup.find('a', id="xxx")
    （5）find_all：找到所有符合要求的标签
        - soup.find_all('a')
        - soup.find_all(['a','b']) 找到所有的a和b标签
        - soup.find_all('a', limit=2)  限制前两个
    （6）根据选择器选择指定的内容
               select:soup.select('#feng')
        - 常见的选择器：标签选择器(a)、类选择器(.)、id选择器(#)、层级选择器
            - 层级选择器：
                div .dudu #lala .meme .xixi  下面好多级
                div > p > a > .lala          只能是下面一级
        【注意】select选择器返回永远是列表，需要通过下标提取指定的对象
"""
import requests
from bs4 import BeautifulSoup
import lxml
import os

if __name__ == '__main__':
    if not os.path.exists('./sanguo'):
        os.mkdir('./sanguo')

    url = 'http://www.shicimingju.com/book/sanguoyanyi.html'
    headers = {
        # 定制请求头中的User-Agent参数，当然也可以定制请求头中其他的参数
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    }
    respnose = requests.get(url=url, headers=headers).text
    # 数据解析
    soup = BeautifulSoup(respnose, 'lxml')
    a_list = soup.select('.book-mulu a')  # 列表
    for a in a_list:
        detail_url = 'http://www.shicimingju.com' + a['href']  # print(a['href']) #/book/sanguoyanyi/1.html
        title = a.string

        detail_page_text = requests.get(url=detail_url, headers=headers).text
        detail_soup = BeautifulSoup(detail_page_text, 'lxml')
        div_tag = detail_soup.find('div', class_='chapter_content')
        content = div_tag.text

        file_path = './sanguo/' + title
        with open(file_path + '.html', 'w', encoding='utf-8') as f:
            f.write(content)
            print(title, 'success!!!!!')

    print('over!')
