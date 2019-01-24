import requests
import json
import lxml
from bs4 import BeautifulSoup

url = 'https://ac.qq.com/ComicView/index/id/505430/cid/928'

sc = requests.get(url)



response = requests.get(url)
#soup = BeautifulSoup(sc.text, 'lxml').content()
py_data = json.loads(response.text)
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
