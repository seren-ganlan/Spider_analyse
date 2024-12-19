import requests

# 定义有效的请求头
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "max-age=0",
    "cookie": "s_fid=3A21C19D5B24D45D-24F6044CF700F5CD; s_cc=true; s_vi=[CS]v1|33AFC85A27D6D28A-60001275A0525842[CE];",
    "if-modified-since": "Sun, 15 Dec 2024 03:02:01 GMT",
    "if-none-match": '"1734231721"',
    "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}

# 请求的URL
url = "https://www.cancer.gov/search/results?swKeyword=nicotine"

# 禁用代理，发送GET请求
response = requests.get(url, headers=headers, proxies={"http": None, "https": None})


# 判断响应状态码
if response.status_code == 200:
    print("Request Successful!")
    # 打印网页内容（可以进一步解析）
    print(response.text)
else:
    print(f"Failed to retrieve content: {response.status_code}")
