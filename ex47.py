import requests
import json

response = requests.get("https://www.douyu.com/gapi/rkc/directory/2_201/0")


py_data =json.loads(response.text)
for i in py_data['data']['rl']:
    print(i['rs16'])
    img_name = i['nn'] + ".jpg"
    content = requests.get(i['rs16']).content
    print("catching ...: "+img_name)
    target = open(img_name,'wb')
    target.write(content)


#print(py_data)