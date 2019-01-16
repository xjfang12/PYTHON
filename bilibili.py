import requests
import json
from fake_useragent import UserAgent
import time

ua = UserAgent()

def Download(url, path):
    ''' Download the movie '''
    size = 0
    # set the starting download time
    start = time.time()

    # construct  request header
    headers = {
        'User-Agent': ua.random
    }

    # mo ni user internet explorer
    # movie ---> data stream
    response = requests.get(url, headers=headers,stream=True)

    # data size each download and total size
    chunk_size = 1024

    #total size
    content_size = int(response.headers('content-length'))

    if response.status_code == 200:
        print('[文件大小]:{}%MB'.format(content_size / chunk_size/ 1024))
        with open(path,'wb') as file:
            for data in response.iter_content(chunk_size=chunk_size):
                file.write(data)
                size += len(data)
                print('\r'+'[下载进度]:{}{}%'.format(">"*int(size * 50 /
                                                         content_size), float(size/content_size * 100)), end=' ')
                end = time.time()
            print('\n' + '视频下载完成!用时: {}'.format(end - start))



def The_url(page):
    url = 'http://api.vc.bilibili.com/board/v1/ranking/top?page_size=10&next_offset=' + str(page) + '&tag=%E4%BB%8A%E6%97%A5%E7%83%AD%E9%97%A8&platform=pc'
    

    headers = {
        'User-Agent': ua.random
    }


    request = requests.get(url,headers=headers).json()

    item = request.get('data').get('items')
    for i in item:
        ite = i.get('item')

        Video_name = ite.get('description')
        #print(Video_name)

        Release_time = ite.get('upload_time')
        #print(Release_time)

        Video_Downloads = ite.get('video_playurl')
        #print(Video_Downloads)

        The_name = i.get('user').get('name')
        #print(The_name)
        


for r in range(0,100):
    r = r * 10 + 1
    The_url(r)
#print (request)
#a = 'http://www.bilibili.com/video/av40046110'
#s = requests.get(a).content()
#fp = open ('a.mp4','wb') 
#fp.write(s)
