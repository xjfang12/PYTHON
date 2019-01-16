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
print(soup)
image = soup.select('.cursor_zoom img')
image_url = image[0].get('src')
res = requests.get(image_url)
with open('bing.jpg','wb') as file:
    file.write(res.content)
