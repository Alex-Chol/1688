import requests
import json
def get_ip():
    #ip_link = 'http://ip.ipjldl.com/index.php/api/entry?method=proxyServer.hdtiqu_api_url&packid=0&fa=0&groupid=0&fetch_key=&time=100&qty=5&port=1&ipport=1&format=json&ss=5&css=&dt=0&pro=&city=&usertype=4'

    # 极光代理
    # 账号17329948370
    link = "http://d.jghttp.golangapi.com/getip?num=1&type=2&pro=0&city=0&yys=0&port=1&pack=23027&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=350000,440000,530000"
    ip_res = requests.get(link).text
    ip_js = json.loads(ip_res)
    ip = ip_js['data'][0]['ip'] +":"+ str(ip_js['data'][0]['port'])
    print("正在使用",ip)
    proxies = {
        'http': 'http://' + ip,
        #'https': 'https://' + ip,
    }

    # 万变IP
    # 账号787001245
    # link = "http://120.79.85.144/index.php/api/entry?method=proxyServer.tiqu_api_url&packid=1&fa=0&dt=&groupid=0&fetch_key=&qty=1&time=6&port=1&format=json&ss=5&css=&dt=&ipport=1&pro=&city=&usertype=6"
    # ip_res = requests.get(link).text
    # ip_js = json.loads(ip_res)
    # print("正在使用",ip_js['data'][0]['IP'])
    # proxies = {
    #     'http': 'http://' + ip_js['data'][0]['IP'],
    #     'https': 'https://' + ip_js['data'][0]['IP'],
    # }
    return proxies