import requests
from bs4 import BeautifulSoup
import os
import datetime

dt = datetime.datetime.now()
print (dt)
cd = str(dt.year)+'0'+str(dt.month)+str(dt.day)
os.makedirs('Bings',exist_ok=True)
url='http://bingwallpaper.com/'
sc=requests.get(url)
soup =BeautifulSoup(sc.text,'lxml')
#print(soup)
image = soup.select('.cursor_zoom img')
#print(image)
print(">>>>for debug, image[0] =",image[0])
image_url = image[0].get('src')
print(">>>>>>>>for debug, image_url =",image_url)
res = requests.get(image_url)
with open('bing.jpg','wb') as file:
    file.write(res.content)
