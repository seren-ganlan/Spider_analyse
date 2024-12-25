# http协议：服务器和客户端进行数据交互的一种形式
'''
常用请求头信息：
        ——User-Agent：请求载体的身份标识
        ——Connection：请求完毕后是断开链接还是保持连接
常用响应头信息：
        —— Content-Type：服务器响应回客户端的数据类型
https协议：安全的超文本协议（数据加密）
加密方式：
        -对称密钥加密
        -非对称密钥加密
        -证书密钥加密

Requsets模块：python中原生的一款基于网络请求的模块，模拟浏览器发起请求

             accept:浏览器通过这个头告诉服务器，它所支持的数据类型
　　　　　　　　Accept-Charset: 浏览器通过这个头告诉服务器，它支持哪种字符集
　　　　　　　　Accept-Encoding：浏览器通过这个头告诉服务器，支持的压缩格式
　　　　　　　　Accept-Language：浏览器通过这个头告诉服务器，它的语言环境
　　　　　　　　Host：浏览器通过这个头告诉服务器，想访问哪台主机
　　　　　　　　If-Modified-Since: 浏览器通过这个头告诉服务器，缓存数据的时间
　　　　　　　　Referer：浏览器通过这个头告诉服务器，客户机是哪个页面来的 防盗链
　　　　　　　　Connection：浏览器通过这个头告诉服务器，请求完后是断开链接还是何持链接
　　　　　　　　X-Requested-With: XMLHttpRequest 代表通过ajax方式进行访问
　　　　　　　　User-Agent：请求载体的身份标识

'''

import requests
import time

def baidu_search(keyword):
    # 使用Session保持会话
    session = requests.Session()

    # HTTP头伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0',
    }

    # 请求URL
    url = 'https://www.baidu.com/s'

    # 请求参数
    params = {'wd': keyword}

    try:
        # 发送请求
        response = session.get(url, headers=headers, params=params, timeout=10)
        response.raise_for_status()  # 检查HTTP状态码
        # 保存搜索结果页面
        with open(f'./baidu_search_{keyword}.html', 'w', encoding='utf-8') as file:
            file.write(response.text)
        print(f"Search results for '{keyword}' saved successfully!")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # 输入搜索关键词
    keyword = input("Enter a keyword to search on Baidu: ")
    # 延时避免频繁请求
    time.sleep(2)  # 等待2秒
    # 开始搜索
    baidu_search(keyword)

