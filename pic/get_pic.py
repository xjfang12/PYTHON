import requests
# import json
from lxml import etree
import re
# a forum page
url = "https://sex8.cc/thread-11969190-1-1.html"



headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36"}

# get the pic
r = requests.get(url,headers=headers) 
ret = r.text   
# over_html = etree.HTML(ret)
# Bittit = over_html.xpath('//td[@class="tf"]/text()')
# print(Bittit)


test = ret.split('\r\n')

lines = []

for line in test:
    if line:
        if '<!--' in line:
            pass
        elif '<img id' in line: 
            # pass
            lines.append(line)

for line in lines:
    tmp=re.match(r'zoomfile=\"(.*)\"',line)
    
    print(">>>>for debug, tmp=",tmp)
# print(repr(ret))
# print(test)
with open('log.txt','w',encoding='utf-8') as f:
    f.write(ret)
# for line in ret:
#     print(line)
# print(">>>> After json:")
# print(json.loads(ret))

#with open('1.jpg','wb') as f:
#    f.write(r.content)