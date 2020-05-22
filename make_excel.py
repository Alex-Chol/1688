from openpyxl import Workbook
class Make_excel(object):
    def __init__(self):
        self.wb = Workbook()

    def openxlsx(self):
        self.ws = self.wb.active
        self.ws.append(['产品标题',"公司名称","联系人姓名","联系电话","联系网址"])

    def insert(self,product_name,company,name,phone_number,connect_link):
        self.ws.append([product_name,company,name,phone_number,connect_link])

    def save(self,now_time):
        self.wb.save('C:/Users/Shinelon/Desktop/'+now_time+'.xlsx')
        return "数据已保存为xlsx"

