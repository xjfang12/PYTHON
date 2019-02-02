import requests
import json
from lxml import etree
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
ua = UserAgent()

headers = {
    'User-Agent': ua.random
}
url = 'https://ac.qq.com/ComicView/index/id/505430/cid/928'

sc = requests.get(url)
html = etree.HTML(sc.text)

print(html)

#soup = BeautifulSoup(sc.text,'lxml')
#with open('soup.txt','w') as file:
 #   file.write(soup.text)
#print(soup)
#result = soup.find_all("ul",class_='comic-contain')
#print(">>>>for debug, result = ",result[0])
#for a in soup:
#   if 'src' in a:
#        print(a,end='\n\n')
#response = requests.get(url)
#soup = BeautifulSoup(sc.text, 'lxml').content()
#py_data = json.loads(response.text)
#print(py_data)
#with open("soup.txt",'w') as file:
#    file.write(py_data)
#src = soup.select('mainView')
#print(src)
#image = soup.select('.cursor_zoom img')
#image_url = image[0].get('src')
#res = requests.get(image_url)
#with open('bing.jpg', 'wb') as file:
 #   file.write(res.content)
