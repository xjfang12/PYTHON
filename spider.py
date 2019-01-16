import requests
import json
import html

response = requests.get("https://ypy.douban.com/explore")
print(response.text)
a = response.text
b = []
for i in a:
    if "img src" in i:
        print(i)
        b.append(i)  
print(b)

py_data = json.loads(response.text)
for i in py_data['data']['rl']:
    print(i['rs16'])
    img_name = i['nn'] + ".jpg"
    content = requests.get(i['rs16']).content
    print("catching ...: "+img_name)
    target = open(img_name, 'wb')
    target.write(content)


#print(py_data)
