import requests
import re
import useragent
import random
import ip_pool
class Html_request(object):
    def __init__(self):
        self.req = requests.session()
        self.proxy = ip_pool.get_ip()
    def get_list_response(self,index):
        # 请求20个商家信息
        
        link = "https://search.1688.com/service/marketOfferResultViewService?keywords=%CF%B4%BB%A4&n=y&netType=1%2C11&encode=utf-8&spm=a260k.dacugeneral.search.0&async=true&asyncCount=20&beginPage=1&pageSize=60&requestId=1191291141831589875120756000550&startIndex="+str(index)
        r = self.req.get(link,headers=self.header1).text

        # 写入测试文件
        # f = open('list.txt','w+',encoding="utf-8")
        # f.write(r.text)
        # f.close()

        # 读取测试文件
        # f = open('list.txt','r+',encoding="utf-8")
        # r = f.read()
        # f.close()

        return r
 
    def get_connect_response(self,link):
        keys = re.compile('https://(.+)/page')
        key = re.compile('http://(.+)/page')
        host = keys.findall(link)
        if len(host) == 0:
            host = key.findall(link)
        try:
            host = host[0]
        except:
            print("构造请求头出错啦！")
            exit()

        header_connect = {
            'Host': host,
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0",
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'DNT': '1',
            'Connection': 'close',
            'Upgrade-Insecure-Requests': '1',
            'Cache-Control': 'max-age=0',
        }
        #获取方式页面的源代码
        #now = time.strftime('%Y%m%d%H%M%S',time.localtime())

        # 获取代理IP
        
        try:
            r = self.req.get(link,headers=header_connect,allow_redirects=True,timeout=5,proxies=self.proxy)
            #print(r.status_code,r.text)
            if r.status_code == 200 or r.status_code == 301:
                # f = open(str(now)+'.txt','a+',encoding="utf-8")
                # f.write(r.text)
                # f.close()
                return r.text
            else:
                print("获取商家信息时出现未知错误！")
                exit()
        except:
            num = 1
            while num < 11:
                num += 1
                print("请求出错，切换IP重新访问...")
                self.proxy = ip_pool.get_ip() # IP已经失效，因此改变IP
                # 这里的程序逻辑是：当目前IP超时时，更改IP，并使用新IP重新请求链接。
                print('第%s次重复请求' % (num-1))
                # 调用 重连函数 进行重连
                response = self.reconnect_link(link,header_connect)
                if response != None:
                    return response


    def reconnect_link(self,link,re_header):
        try:
            return self.req.get(link,headers=re_header,timeout=5,proxies=self.proxy).text
        except:
            print("IP失效，更换IP")
            return None

        

# 请求头需要设置一个池
    header1 = {
        "Accept-Encoding":"gzip, deflate, br",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0",
        "Host":'search.1688.com',
        "Referer":'https://s.1688.com/selloffer/offer_search.htm?keywords=%CF%B4%BB%A4&n=y&netType=1%2C11&encode=utf-8&spm=a260k.dacugeneral.search.0',
        "TE":"Trailers"
    }

    # 注意：cookies的h_keys需要改为：%u6d17%u62a4

    data = {"keywords":"%CF%B4%BB%A4","n":"y","netType":"1,11","encode":"utf-8","spm":"a260k.dacugeneral.search.0","async":"true","asyncCount":"20","beginPage":"1","pageSize":"60","requestId":"1191291141831589865527372000549","startIndex":"20"}
        # asyncreq 为换页参数
        
# a = Html_request()
# print(a.get_list_response())
