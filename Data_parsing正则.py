import requests
import re
import os

if __name__ == '__main__':
    url = 'http://jandan.net/ooxx'
    headers = {
        # 定制请求头中的User-Agent参数，当然也可以定制请求头中其他的参数
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    }
    # 创建文件
    if not os.path.exists('./pics'):
        os.mkdir('./pics')

    # 使用通用爬虫爬取整张页面
    page_text = requests.get(url=url, headers=headers).text

    # 使用聚焦爬虫
    ex = '<img src="(.*?)".*?>'
    img_src_list = re.findall(ex, page_text, re.S)
    for img_src in img_src_list:
        img_src_url = 'https:' + img_src

        pic_bytes = requests.get(url=img_src_url, headers=headers).content
        pic_name = img_src_url.split('/')[-1]
        pic_path = './pics/' + pic_name
        with open(pic_path, 'wb') as f:
            f.write(pic_bytes)
            print(pic_name, 'ok!')
