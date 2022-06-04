# Charging_point
充电桩调度系统用户侧记录

# 0604
## 待完成模块
- 用户
  - id
  - name
  - passwd
  - 余额
  - 订单(list[class])
- 订单
  - 订单号
  - 用户id
  - 详单生成时间
  - 充电桩编号
  - 充电模式
  - 充电电量
  - 充电时长
  - 启动时间
  - 停止时间
  - 充电费用
  - 服务费用
  - 总费用
  - 是否已经完成

ord_id
usr_id
ord_gene_time
ch_id
ch_mode
ch_capacity
ch_time
start_time
stop_time
ch_pay
serve_pay
sum_pay
is_finish




- 可完成
- 用户(yzf)
  - 注册
  - 登录
  - 修改密码
  - 充值余额
  - 扣除余额
  - 发起请求 (wly)
    - 提交充电请求(服务端->初始化详单)
    - 修改充电请求
    - 查看车辆排队号码
    - 查看等待数量
    - 结束充电


- 详单(yzf)
  - 初始化
  - 打印详单


1 m 5 5
