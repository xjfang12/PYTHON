#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
# from lxml import etree

url = 'https://ac.qq.com/ComicView/index/id/505430/cid/928'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36"}

r = requests.get(url,headers=headers)
soup = BeautifulSoup(r.text,"lxml")
print(soup)






# page_list = r.split('\r\n')
# for line in page_list:
#     if line.strip().startswith('<img src'):
#         print(line.strip())
# print(repr(sc.text))
# html = etree.HTML(sc.text)
# print(html)
# Img_list = html.xpath('//ul[@class="comic-contain"]/li/@img src')

# print(Img_list)






def getImageUrls(comic_url):
    """
    通过Selenium盒Phantojs获取动态生成数据
    """
    urls = []
    dcap = dict(DesiredCapabilities.PH)

