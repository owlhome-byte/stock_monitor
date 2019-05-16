from datetime import datetime
from handleconfig import HandleConfig
from dingding import SendMsg
from stock import Stock

import time

class Warning():
    def __init__(self):
        self.config = HandleConfig()
        self.stock = Stock()
        self.sell = '可以卖啦'
        self.end = '加仓!加仓!加仓!'

    def send_msg(self,msg):
        return SendMsg().send_msg(msg)

    def handle_each_section(self, section):
        stock_code = section.get('code', ' ')
        max_price = float(section.get('max_price', 0))
        min_price = float(section.get('min_price', 0))

        self.stock.code = stock_code
        stock_info = self.stock.get_stock_info()

        if not stock_info:
            print('没有股价信息')
            return

        msg = ''
        now = datetime.now().strftime('%m-%d %H:%M:%S')

        if float(stock_info['price']) >= max_price:
            msg = "{1}-现价:{2},已经超过{3};{4}时间:{0}".format(
                                                    now,
                                                    stock_info['name'],
                                                    float(stock_info['price']),
                                                    max_price,
                                                    self.sell,


            )
            print(msg)
            return self.send_msg(msg)
        elif float(stock_info['price']) <= min_price:
            msg = "{1}-现价:{2},已经超过{3};{4}时间:{0}".format(
                                                    now,
                                                    stock_info['name'],
                                                    float(stock_info['price']),
                                                    min_price,
                                                    self.end,
            )
            print(msg)
            return self.send_msg(msg)
        else:
            print('In moniting 时间{}'.format(now))
            return True

    def monitor(self):
        while True:
            sections = self.config.get_read()
            for section in sections:
                section = dict(section)
                res = self.handle_each_section(section)
                if not res:
                    return
                s_time = section.get('interval')
                print('sleep{}'.format(s_time))
                time.sleep(int(s_time))


if __name__ == '__main__':
    warning = Warning()
    warning.monitor()