"""
定义一个门票系统
门票的原价是100元
当周末的时候门票涨价20%
小孩子半票
计算2个成人和1个小孩的平日票价
"""
class Ticket():
    def __init__(self,weekday=False,child=False):
        self.exp = 100
        if weekday:
            self.inc = 1.2
        else:
            self.inc = 1
        if child:
            self.discount = 0.5
        else:
            self.discount = 1
    def cal_price(self,nun):
        return self.exp+self.inc*self.discount+nun

tk =