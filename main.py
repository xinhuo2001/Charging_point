from time import sleep
from user import User
import json

#读入用户数据文件 返回List
def readUserData():
    userDataPath = "./usrdata.json"
    with open(userDataPath, 'r', encoding='utf-8') as f:
        content = f.read()
        content_list = json.loads(content)
    return content_list

#展示一个用户字典里面的数据
def showUserDict(udict):
    id = udict.get("id","null")
    name = udict.get("name","null")
    passwd = udict.get("passwd","null")
    balance = udict.get("balance","null")
    orderList = udict.get("orderList","null")
    print(f"基本信息:id:{id} 姓名:{name} 密码:{passwd} 余额:{balance} ")
    print("订单信息")
    for order in orderList:
        showOrderDict(order)

#将用户总列表的内容写回文件
def saveUserInfo(user_list):
    userDataPath = "./usrdata2.json"
    user_str = json.dumps(user_list)
    print(user_str)
    with open(userDataPath, "w", encoding='utf-8') as f:
        f.write(user_str)
    pass

#展示一个订单字典里面的数据
def showOrderDict(odict):
    ord_id = odict.get("ord_id", "null")
    usr_id = odict.get("usr_id", "null")
    sum_pay = odict.get("sum_pay", "null")
    is_finish = odict.get("is_finish", "null")
    print(f"订单: 编号:{ord_id} 用户id:{usr_id} 金额:{sum_pay} 是否完成:{is_finish} ")

#登录 成功返回用户信息 失败返回None
def userLogin(name, passwd, user_list):
    #遍历list 判断是否有当前用户
    for user in user_list:
        if user["name"] == name:
            if user["passwd"] == passwd:
                print(f"{name} 登录成功...")
                return user
            else:
                print(f"{name}:密码错误 登录失败...")
            break
    print(f"{name} 还未注册 请先注册再登录")
    return None

#根据账号 密码初始化一个用户字典
def initUserDict(id, name, passwd):
    user = dict()
    user["id"] = id
    user["name"] = name
    user["passwd"] = passwd
    user["balance"] = 0
    user["orderList"] = []
    return user

#注册 成功返回用户字典 失败返回None
def userRegister(name, passwd, user_list):
    id = -1
    for user in user_list:
        #为当前用户确立id 最大id+1
        if id < user["id"]:
            id = user["id"]
        if user["name"] == name:
            print(f"{name} 该账号明已被注册, 注册失败...")
            return None
    id += 1
    print(f"{name} 注册成功")
    return initUserDict(id, name, passwd)


#修改密码
def userModifyPasswd(oldPasswd, newPasswd):
    pass

#充值余额
def rechargeBalance(count):
    pass

#扣除余额
def deductionBalance(count):
    pass

#测试模块
def test():
    user_list = readUserData()
    # print(user_list)

    for i in range(len(user_list)):
        print(f'第{i}个用户:')
        showUserDict(user_list[i])
        print("\n")

    print("+++++++++++++++++++++++")
    #注册流程
    name = "王五"
    passwd = "789"
    ruser = userRegister(name, passwd, user_list)
    if ruser != None:
        user_list.append(ruser)
    
    print("+++++++++++++++++++++++")
    for i in range(len(user_list)):
        print(f'第{i}个用户:')
        showUserDict(user_list[i])
        print("\n")

    print("+++++++++++++++++++++++")
    name = "王五"
    passwd = "789"
    ruser = userRegister(name, passwd, user_list)
    if ruser != None:
        user_list.append(ruser)
    
    print("+++++++++++++++++++++++")
    for i in range(len(user_list)):
        print(f'第{i}个用户:')
        showUserDict(user_list[i])
        print("\n")

    print("+++++++++++++++++++++++")
    name = "王五"
    passwd = "789"
    luser = userLogin(name, passwd, user_list)
    
    print("+++++++++++++++++++++++")
    if luser != None:
        showUserDict(luser)
    saveUserInfo(user_list)

if __name__ == "__main__":
    test()
    pass