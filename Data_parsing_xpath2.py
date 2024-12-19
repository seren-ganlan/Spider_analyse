import requests
from lxml import etree
import os

if __name__ == '__main__':
    url = 'http://pic.netbian.com/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Cookie': 'cf_clearance=yDcLvpkYD4Y1K08j.jrjh2vEkWzJRf.TyE.lCpECtfw-1734276451-1.2.1.1-WUa68CpXf7a1CX9UYWCsS9UfX6QvPkClz1UNvYo35m2xqctCbufBgXf_U2z2n4fgS9J280LI8kR86bC8BVounZs2xX.VF0UaJ0Tfs11TXwZd1yL1ItvPMD8kZpUTv_6othgLOd.zkkXvoTs_QeQum.0FhXp9bzd70PclEhdoW.c4yMtNXWAUG0oXH0C6Trh7fQevCy_.FcJP._LPTqnoJaItMpo2B6jDa8FLNJi_167ZiBgoVWeidMZ7Ov3veSaWdLXxvNVYDOt8.5E1GQxS7X0j7wB68hE_PzsKpwpXEGP2LuUwltSbLJOzi_ntYI7XYw_hztTTEloNue6j7hNSH0p_NOhy4GkpzIlgxeNP_SiuURwbwO5LayDdRm_6Ps16MVXDZvH.x5KtfC5fp7jEW1pHk5v7akXZIM70AL2U.niKVZf3ScYu5M8gqxHfCNvx; zkhanecookieclassrecord=%2C54%2C'  # 替换为实际浏览器捕获的Cookie
    }

    # 爬取页面源码数据
    response = requests.get(url=url, headers=headers)
    # response.encoding = 'GBK'  # 根据页面的实际编码设置
    page_text = response.text
    print(page_text)

    # 数据解析
    tree = etree.HTML(page_text)
    print(tree)


    # 调整 XPath 表达式，选择 `ul` 标签下的所有 `li` 标签
    li_list = tree.xpath('//div[@class="slist"]/ul[@class="clearfix"]/li')

    # 创建图片存储目录
    if not os.path.exists('./picLibs'):
        os.mkdir('./picLibs')

    # 遍历 li 列表并处理每个图片信息
    for li in li_list:
        try:
            # 构造图片完整 URL
            img_src = url + li.xpath('./a//img/@src')[0]

            # 获取图片的 alt 属性作为文件名
            img_name = li.xpath('./a//img/@alt')[0] + '.jpg'

            # 修正文件名编码问题
            img_name = img_name.encode('iso-8859-1').decode('gbk')

            # 下载图片并保存
            img_data = requests.get(url=img_src, headers=headers).content
            with open(f'./picLibs/{img_name}', 'wb') as f:
                f.write(img_data)
                print(f'{img_name} - success!')
        except Exception as e:
            print(f'Error processing an image: {e}')
