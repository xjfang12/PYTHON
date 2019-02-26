import requests
from lxml import etree
import os

def start_request():
    request = requests.get('https://sex8.cc/thread-11537602-1-1.html')
    html = etree.HTML(request.text)
    Bittit = html.xpath('//div[@class="mbn savephotop"]/text()')
    print(Bittit)


start_request()