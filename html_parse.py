import json
from lxml import etree
class Html_parse(object):
    def __init__(self):
        pass
    def list_parse(self,response):
        js = json.loads(response)
        product_name = []
        connect_link = []
        for i in range(len(js['data']['data']['offerList'])):
            product_name.append(js['data']['data']['offerList'][i]['information']['simpleSubject'])
            # 公司名字
            #company.append(js['data']['content']['offerResult'][i]['attr']['company']['name'])

            # creditdetail替换成contactinfo 构成联系方式的url
            connect_link.append(js['data']['data']['offerList'][i]['tradeService']['tpCreditUrl'].replace("creditdetail","contactinfo"))
            #connect_link.append(js['data']['data']['offerList'][i]['tradeService']['tpCreditUrl'])
        return product_name,connect_link

    def connect_parse(self,response):
        # 手机号
        # //dl[@class='m-mobilephone']/dd/text()
        # //dl[@class="m-mobilephone"]/@data-no
        # 公司名
        # //div[@class='contact-info']/h4/text()
        # 联系人姓名
        # //div[@class='contact-info']//a[@class='membername']/text()
        html = etree.HTML(response)
        m_phone = html.xpath("normalize-space(//dl[@class='m-mobilephone']/dd/text())")
        if m_phone == '':
            m_phone = html.xpath('normalize-space(//dl[@class="m-mobilephone"]/@data-no)')
        company = html.xpath("normalize-space(//div[@class='contact-info']/h4/text())")
        name = html.xpath("normalize-space(//div[@class='contact-info']//a[@class='membername']/text())")
        return m_phone,company,name

# a = Html_parse()
# f = open('list.txt','r+',encoding="utf-8")
# r = f.read()
# f.close()
# print(a.list_parse(r))