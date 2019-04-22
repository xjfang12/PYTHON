#import requests
#
#url = "http://audio.xmcdn.com/group60/M09/49/CD/wKgLb1yvS6PRCRkNABmsv_x0Wy4336.m4a"
#
#with open('1.m4a', 'wb') as f:
#    r = requests.get(url)
#    f.write(r.content)

import requests
import json
import threading


def xiMa(i):
    # 1. get the url
    url = "https://www.ximalaya.com/revision/play/album?albumId=291718&pageNum=" + str(i) + "&sort=-1&pageSize=30"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36"}
    # 2. get the data
    r = requests.get(url, headers=headers)
    # print(r)
    ret = r.text             # json type string, outside is ''', inside is '"'
    print(ret)
    result = json.loads(ret) # json string to dict
    # print(type(result))
    content_list = result['data']['tracksAudioPlay']
    # print(result['data']['tracksAudioPlay'][29])

    for content in content_list:
        # print(content)
        download_url = content['src']
        download_name = content['trackName']
        # print(download_name, '+', download_url)
        # music_name = download_name + '.m4a'
        with open('mp3/%s.m4a' % download_name, 'wb') as f:
            print("In downloading", download_name,'....')
            r = requests.get(download_url)
            f.write(r.content)
        # print(tmp)


if __name__ == '__main__':
    for i in range(10):
        # xiMa(i+1)
        t=threading.Thread(target=xiMa,args=(i+1,))
        t.start()