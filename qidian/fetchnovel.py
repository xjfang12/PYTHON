import requests
from lxml import etree
import os

# 面向对象设计模式 集成封装
class Spider(object):
    def start_request(self):
        # 1. 请求拿到小说名创建文件夹
        response = requests.get("https://www.qidian.com/all")
        html = etree.HTML(response.text)
        Bigtit_list = html.xpath('//div[@class="book-mid-info"]/h4/a/text()')  
        Bigsrc_list = html.xpath('//div[@class="book-mid-info"]/h4/a/@href')
        for Bigtit,Bigsrc in zip(Bigtit_list, Bigsrc_list):
            #print(Bigtit,Bigsrc)
            if os.path.exists(Bigtit) == False:
                os.makedirs(Bigtit)
            self.file_data(Bigtit,Bigsrc)

    def file_data(self,Bigtit, Bigsrc):
        # 2. 请求拿到每本小说每一章名
        response = requests.get("http:" + Bigsrc)
        html = etree.HTML(response.text)
        Littit_list = html.xpath('//ul[@class="cf"]/li/a/text()')
        Litsrc_list = html.xpath('//ul[@class="cf"]/li/a/@href')
        #print(Littit_list,Litsrc_list)
        for Littit,Litsrc in zip(Littit_list,Litsrc_list):
            self.finally_file(Littit,Litsrc,Bigtit)
            #print(Littit,Litsrc)
            #if os.path.exists(Littit) == False:
                
    def finally_file(self, Littit, Litsrc, Bigtit):
        # 3. 创建文件，每章内容写入文件
        response = requests.get("http:"+ Litsrc)
        html = etree.HTML(response.text)

        # list ==> str
        content = "\n".join(html.xpath('//div[@class="read-content j_readContent"]/p/text()'))

            
        file_name = Bigtit + "\\" + Littit + ".txt"
        print("正在抓取文章：" + file_name)
        with open(file_name,"a", encoding="utf-8") as f:
            f.write(content)


spider =Spider()
#spider.finally_file("凡人修仙传", '//read.qidian.com/chapter/ORlSeSgZ6E_MQzCecGvf7A2/atYOCLHSg35Ms5iq0oQwLQ2')
spider.start_request()
