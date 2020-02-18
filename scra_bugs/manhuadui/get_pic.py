import requests
from lxml import etree


url = 'https://www.manhuadui.com/manhua/nvzixueyuandenansheng/329825.html'

response = requests.get(url)
html = etree.HTML(response.text)
src_list = html.xpath('//div[@class="comic_wraCon autoHeight"]')
for i in src_list:
    print(i)

url1 = 'https://mhcdn.manhuazj.com/images/comic/165/329825/15647208207063298250b3039b83.jpg'
url2 = 'https://mhcdn.manhuazj.com/images/comic/165/329825/15647208233273298251fd3534c5.jpg'

response = requests.get(url1)
with open("1.jpg",'wb') as f:
    f.write(response.content)
    f.close()

response = requests.get(url2)
with open("2.jpg",'wb') as f:
    f.write(response.content)
    f.close()
    
