# import random
# import time
# import requests
# from bs4 import BeautifulSoup
# import csv
#
# # # 指定搜索关键字
# # kwd = 'vape'
#
# def getAllRrl(kwd, pages):  # 增加 pages 参数，控制爬取页数
#     headers = {
#         "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
#     }
#     # 打开CSV文件以写入数据
#     with open(f'{kwd}.csv', mode='w', newline='', encoding='utf-8') as file:
#         writer = csv.writer(file)
#         writer.writerow(['rank', 'title', 'url'])  # 写入表头
#
#         for page in range(pages):  # 循环爬取多页
#             start = page * 10  # 计算 start 参数，每页 10 条
#             url = f'https://www.google.com/search?q={kwd}&start={start}'  # 添加 start 参数控制页码
#
#             # 发起请求
#             response = requests.get(url, headers=headers)
#             if response.status_code != 200:
#                 print('请求失败')
#                 return
#
#             rlt01 = BeautifulSoup(response.text, 'html.parser')
#             rlt02 = rlt01.find_all('div', class_='tF2Cxc')
#
#             for rank, result in enumerate(rlt02, start=1 + page * 10):  # 修改 rank，保持全局排名
#                 title = result.find('h3').text
#                 url = result.find('a')['href']
#                 print('rank:', rank)
#                 print('title:', title)
#                 print('url:', url)
#                 # 将数据写入 CSV 文件
#                 writer.writerow([rank, title, url])
#             time.sleep(random.uniform(10, 20))  # 随机延迟，防止被封禁
# # 获取用户输入的搜索关键字
# kwd = input("请输入搜索关键字: ")
# # 获取用户输入的要爬取的页数
# try:
#     pages = int(input("请输入要爬取的页数: "))
#     if pages <= 0:
#         print("页数必须是正整数。")
#     else:
#         # 调用函数，指定爬取指定页数的结果
#         getAllRrl(kwd, pages)
# except ValueError:
#     print("请输入有效的页数（正整数）。")


import random
import time
import requests
from bs4 import BeautifulSoup
import csv

proxyAddr = "overseas.tunnel.qg.net:14280"
authKey = "CRLVETYX"
password = "1F63F5166B34"
proxyUrl = "http://%(user)s:%(password)s@%(server)s" % {
    "user": authKey,
    "password": password,
    "server": proxyAddr,
}
proxies = {
    "http": proxyUrl,
    "https": proxyUrl,
}
def getAllRrl(kwd, pages):  # 增加 pages 参数，控制爬取页数
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    }

    # 打开CSV文件以写入数据
    with open(f'{kwd}.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['rank', 'title', 'url'])  # 写入表头

        # 循环爬取多页
        for page in range(pages):
            start = page * 10  # 计算 start 参数，每页 10 条
            url = f'https://www.google.com/search?q={kwd}&start={start}'  # 添加 start 参数控制页码

            try:
                # 发起请求并处理异常
                response = requests.get(url, headers=headers,proxies=proxies)
                response.raise_for_status()  # 如果响应状态码不是 200，将抛出异常

            except requests.exceptions.RequestException as e:
                print(f"请求失败: {e}")
                return

            # 解析 HTML 内容
            rlt01 = BeautifulSoup(response.text, 'html.parser')
            rlt02 = rlt01.find_all('div', class_='tF2Cxc')

            # 解析每一页的搜索结果
            for rank, result in enumerate(rlt02, start=1 + page * 10):  # 修改 rank，保持全局排名
                title = result.find('h3').text
                link = result.find('a')['href']
                print(f'rank: {rank}')
                print(f'title: {title}')
                print(f'url: {link}')

                # 将数据写入 CSV 文件
                writer.writerow([rank, title, link])

            # 随机延迟，防止被封禁
            time.sleep(random.uniform(1, 3))  # 延迟 6 到 8 秒之间


# 获取用户输入的搜索关键字
kwd = input("请输入搜索关键字: ")

# 获取用户输入的要爬取的页数
try:
    pages = int(input("请输入要爬取的页数: "))
    if pages <= 0:
        print("页数必须是正整数。")
    else:
        # 调用函数，指定爬取指定页数的结果
        getAllRrl(kwd, pages)
except ValueError:
    print("请输入有效的页数（正整数）。")
