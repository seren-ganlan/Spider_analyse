import requests
import csv
from bs4 import BeautifulSoup
import time
import random
import json

# 发起请求的URL链接地址
base_api_url = "https://www.2firsts.com/index.php/api/v2/page/get"

# 文章链接的URL前半部分
base_url = "https://www.2firsts.com/news/"

# 定义 HTTP 请求头伪装
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Connection": "keep-alive",
    "Accept-Language": "en-US,en;q=0.9",
}

# 获取文章的url地址
def get_url(page, limit):
    # 构造完整的 API URL
    api_url = f"{base_api_url}?type=11&page={page}&limit={limit}"
    print("请求的 URL:", api_url)

    try:
        # 发送请求获取数据
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()  # 检查 HTTP 响应状态码

        # 解析 JSON 数据
        data = response.json()
        #文章url后缀获取
        # 提取 list 和 links 中的 seo_url
        list_urls = [item['seo_url'] for item in data.get('data', {}).get('list', []) if 'seo_url' in item]
        # 提取 `links` 中的所有 `seo_url`
        link_urls = [item['seo_url'] for sub_item in data.get('data', {}).get('list', []) for item in
                     sub_item.get('links', []) if 'seo_url' in item]
        # 所有文章url的后缀
        article_urls = list_urls + link_urls
        # 拼接完整文章URL链接
        all_urls = [base_url + url for url in article_urls]
        print(f"获取到的文章链接数量: {len(all_urls)}")
        # 返回文章的url链接
        return all_urls
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")
        return []
    except json.JSONDecodeError:
        print("JSON 数据解析失败！")
        return []
    except KeyError:
        print("数据解析错误，字段可能不存在！")
        return []

# 定义获取文章标题和内容以及图片url链接
def get_post(article_links):
    """
    爬取文章内容并保存到 CSV
    """
    #新建news.csv文件
    with open('news.csv', mode='w', newline='', encoding='utf-8') as file:
        # 定义写入
        writer = csv.writer(file)
        writer.writerow(['articleId', 'title', 'content', 'urlOriginal', 'img_url'])  # 写入表头

        article_id = 1  # 初始化索引文章 ID
        # 遍历url链接
        for url in article_links:
            try:
                # 对url链接发起请求
                response = requests.get(url, headers=headers)
                # 检查是否有HTTP错误
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                print(f"请求失败: {e}")
                continue

            # 假设 response 是请求得到的 HTML 响应
            soup = BeautifulSoup(response.text, 'html.parser')

            # 查找文章容器
            article = soup.find('div', class_='article-box')

            # 初始化标题、内容、图片 URL
            title = ''
            content = ''
            img_url = ''

            if article:
                # 提取文章标题
                title_tag = article.find('h1', class_='harmony-bold title')
                title = title_tag.text.strip() if title_tag else ''

                # 提取所有 ck content 的文本内容
                content_tags = article.find_all('div', class_='ck content')
                content = "\n".join(tag.get_text(strip=True) for tag in content_tags) if content_tags else ''

                # 查找第一个 <figure class="image"> 下的 <img> 标签
                img_tag = article.find('div', class_='image').find('img') if article.find('div',class_='image') else ''
                if img_tag and 'data-src' in img_tag.attrs:
                    img_url = img_tag['data-src']
                else:
                    img_url = ''  # 无图则以空值处理
                # 写入 CSV 文件
                writer.writerow([article_id, title, content, url, img_url])
                print(f"写入文章 ID: {article_id}, 标题: {title}")
                # 更新文章 ID
                article_id += 1
            # 延迟，避免被封禁
            time.sleep(random.uniform(1, 3))


if __name__ == "__main__":
    # 用户输入页码和限制
    page = int(input("请输入页数 (page): "))
    limit = int(input("请输入每页限制的文章数量 (limit): "))

    # 获取文章链接列表
    article_links = get_url(page, limit)
    print(article_links)

    if article_links:
        # 爬取文章内容
        get_post(article_links)
    else:
        print("未获取到任何文章链接！")

