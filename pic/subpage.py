import requests
# import json
import re


url = "https://sex8.cc/forum-710-1.html"

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36"}

r = requests.get(url, headers=headers)
# print(r.text)
# html_lines = r.text.split('\r\n')
ret = r.text.split('\r\n')
for line in ret:
    if line.strip().startswith('<a href'):
        # if 'class="sxst"' in line:
            print(line)
        # with open('debug.txt', 'w') as f:
        #     f.write(line)
    # print(line)