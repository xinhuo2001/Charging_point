class Order:
    orderCount = 0

    def __init__(self, ord_id, usr_id, ord_gene_time, ch_id, ch_mode, ch_time, 
                ch_capacity, start_time, stop_time, ch_pay, serve_pay, sum_pay, is_finish):
        self.ord_id = ord_id #订单号
        self.usr_id = usr_id #用户id
        self.ord_gene_time = ord_gene_time #详单生成时间
        self.ch_id = ch_id #充电桩编号
        self.ch_mode = ch_mode  #充电模式
        self.ch_time = ch_time #充电时长
        self.ch_capacity = ch_capacity #充电电量
        self.start_time = start_time #启动时间
        self.stop_time = stop_time #停止时间
        self.ch_pay = ch_pay #充电费用
        self.serve_pay = serve_pay #服务费用
        self.sum_pay = sum_pay #总费用
        self.is_finish = is_finish #是否已经完成
    
    def showData(self):
        print(f'订单号:{self.ord_id}')        
        print(f'用户id:{self.usr_id}')
        print(f'详单生成时间:{self.ord_gene_time}')
        print(f'充电桩编号:{self.ch_id}')
        print(f'充电模式:{self.ch_mode}')
        print(f'充电电量:{self.ch_time}')
        print(f'充电时长:{self.ch_capacity}')
        print(f'启动时间:{self.start_time}')
        print(f'停止时间:{self.stop_time}')
        print(f'充电费用:{self.ch_pay}')
        print(f'服务费用:{self.serve_pay}')
        print(f'总费用:{self.sum_pay}')
        print(f'是否已经完成:{self.is_finish}')








        