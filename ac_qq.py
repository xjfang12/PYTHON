import requests
from lxml import etree

url = 'https://ac.qq.com/ComicView/index/id/505430/cid/928'

sc = requests.get(url)
html = etree.HTML(sc.text)
Img_list = html.xpath('//ul[@class="comic-contain"]/li/@img src')

print(Img_list)

