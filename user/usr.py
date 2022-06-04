import json
import order
from user.order import Order

class User:
    '用户类...'
    userCount = 0 #用户总人数

    #参数含义 id 名字 密码 余额 订单(未定)
    def __init__(self, id, name, passwd, balance, orderList):
        User.userCount += 1
        self.id = id
        self.name = name
        self.passwd = passwd
        self.balance = balance
        self.orderList = orderList
        self.writeInfoToFile()
        
    #个人信息展示
    def showInfo(self):
        print("个人信息如下:")
        print(f'id:{self.id} name:{self.name} passwd:{self.passwd} balance:{self.balance}')
    
    #总人数
    def showUserCount():
        print(f'总注册用户:{User.userCount}')

    #将当前用户信息更新到文件
    def writeInfoToFile(self):
        pass

    def submitRequest(self):
        #输入
        #服务器
        l = Order(1,1,2,1)
        #添加
        self.append(l)
        #重写文件

    
    
