import requests
# import json
from lxml import etree
import re
# a forum page
# url = "https://sex8.cc/thread-11969190-1-1.html"
url = "https://sex8.cc/thread-12004017-1-1.html"
subpage_url = "https://sex8.cc/forum-710-1.html"

def download_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36"}

    # get the pic
    r = requests.get(url, headers=headers)
    html_lines = r.text.split('\r\n')

    for line in html_lines:
        if line:
            if '<!--' in line:
                pass
            elif line.startswith('<img id'):
                tmp = re.search(r'zoomfile\=\"(.*)\"\ file\=', line)
                download_src = tmp.group(1)
                download_name = download_src.split('/')[-1]
                with open(download_name,'wb') as f:
                    print("downloading "+download_name+' ...')
                    f.write(requests.get(download_src).content)
                    f.close()

download_page(url)


