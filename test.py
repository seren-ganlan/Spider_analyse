import requests

# 定义有效的请求头
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}

# 请求的URL
url = "https://www.cancer.gov/search/results?swKeyword=nicotine"

# 禁用代理，发送GET请求
response = requests.get(url, headers=headers)


# 判断响应状态码
if response.status_code == 200:
    print("Request Successful!")
    # 打印网页内容（可以进一步解析）
    print(response.text)
else:
    print(f"Failed to retrieve content: {response.status_code}")
