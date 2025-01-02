import random
import time
import requests
from bs4 import BeautifulSoup
import csv
import tkinter as tk
from tkinter import filedialog
import pandas as pd


# 配置代理（如果不需要代理可删除相关部分）
proxyAddr = "overseas.tunnel.qg.net:16665"
authKey = "T9XJE6QV"
password = "F922B99F3881"
proxyUrl = "http://%(user)s:%(password)s@%(server)s" % {
    "user": authKey,
    "password": password,
    "server": proxyAddr,
}
proxies = {
    "http": proxyUrl,
    "https": proxyUrl,
}

def getAllRrl(kwd, pages):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',

    }
    # 打开 CSV 文件以写入数据
    with open('Website_Information.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Rank', 'Title', 'URL'])  # 写入表头

        # 循环每个关键字
        for kw in kwd:
            print(f"开始爬取关键词: {kw}")
            for page in range(pages):  # 循环爬取多页
                start = page * 10  # 每页10条记录
                url = f'https://www.google.com/search?q={kw}&start={start}'

                try:
                    # 发起请求
                    response = requests.get(url, headers=headers, proxies=proxies)
                    response.raise_for_status()  # 确保返回状态码为200
                except requests.exceptions.RequestException as e:
                    print(f"请求失败: {e}")
                    continue

                # 解析 HTML 内容
                soup = BeautifulSoup(response.text, 'html.parser')
                results = soup.find_all('div', class_='tF2Cxc')

                # 解析每条结果
                for rank, result in enumerate(results, start=1 + page * 10):
                    title = result.find('h3').text
                    link = result.find('a')['href']
                    print(f"Rank: {rank} | Title: {title} | URL: {link}")
                    writer.writerow([rank, title, link])

                # 随机延迟，防止被封禁
                time.sleep(random.uniform(1, 3))  # 随机延迟1到3秒

def select_excel_file():
    """用户选择Excel文件"""
    file_path = filedialog.askopenfilename(
        title="选择Excel文件",
        filetypes=[("Excel文件", "*.xlsx *.xls")]
    )
    if not file_path:
        print("未选择文件")
        return None
    return file_path

def main():
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口

    # 提示用户选择Excel文件
    print("请选择包含 'Keyword' 列的 Excel 文件")
    excel_path = select_excel_file()
    if not excel_path:
        return

    # 读取Excel文件
    try:
        df = pd.read_excel(excel_path)
        if 'Keyword' not in df.columns:
            print("Excel文件中未找到 'Keyword' 列")
            return
        keywords = df['Keyword'].dropna().tolist()  # 获取关键词列表
    except Exception as e:
        print(f"读取Excel文件失败: {e}")
        return

    # 获取用户输入的页数
    try:
        pages = int(input("请输入要爬取的页数: "))
        if pages <= 0:
            print("页数必须是正整数")
            return
    except ValueError:
        print("请输入有效的页数（正整数）")
        return

    # 开始爬取
    getAllRrl(keywords, pages)
    print("爬取完成，结果已保存为 'Website_Information.csv'")

if __name__ == "__main__":
    main()
