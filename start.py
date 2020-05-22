from html_request import Html_request
from html_parse import Html_parse
from make_excel import Make_excel
import time

import random
class main(object):
    def __init__(self):
        self.request = Html_request()
        self.parse = Html_parse()
        self.xlsx = Make_excel()
        self.sum = 0
    def run(self):
        try:
            self.xlsx.openxlsx()
            now = time.strftime('%Y%m%d%H%M%S',time.localtime())
            for page in range(0,100,20):
                product_name,connect_link = self.parse.list_parse(self.request.get_list_response(page))
                m_phone = []
                company = []
                name = []
                for i in range(20):
                    self.sum += 1
                    print("正在爬取第"+str(self.sum)+"个商家")
                    m_phone_temp,company_temp,name_temp = self.parse.connect_parse(self.request.get_connect_response(connect_link[i]))
                    m_phone.append(m_phone_temp)
                    company.append(company_temp)
                    name.append(name_temp)

                    # 程序睡眠，防止爬取速度过快激活滑动验证
                    #time.sleep(random.randint(0,2))
                    #print(product_name[i],company[i],name[i],m_phone[i])
                    if m_phone[i] != '':
                        self.xlsx.insert(product_name[i],str(company[i]),str(name[i]),str(m_phone[i]),str(connect_link[i]))
            #爬取公司名字、产品名字、联系人姓名、联系方式
        except Exception as e:
            print(e)
        finally:
            print(self.xlsx.save(now))
run = main()
run.run()

