import requests
#指定搜索关键字
word = input('enter a word you want to search:')
#自定义请求头信息:UA伪装,将包含了User-Agent的字典作用到请求方法的headers参数中即可
headers={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    }
#指定url，原始url可能是https://www.sogou.com/web?query=撩妹，发现该url携带了参数
url = 'https://www.sogou.com/web'
#封装get请求参数：如果请求携带了参数，则可以将参数封装到字典中结合这requests请求方法中的data/params参数进行url参数的处理
param = {
    'query':word,
}
#发起请求
response = requests.get(url=url,params=param,headers=headers)
#获取响应数据
page_text = response.text
#持久化存储
fileName = word+'.html'
with open(fileName,'w',encoding='utf-8') as fp:
    fp.write(page_text)