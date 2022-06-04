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
        pass