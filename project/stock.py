import tushare as ts


class Stock(object):
    def __init__(self):
        pass

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, stock_code):
        self._code = stock_code

    def get_stock_info(self):
        try:
            stock_info = ts.get_realtime_quotes(self._code)
            return stock_info[['name', 'price']].iloc[0].to_dict()
        except Exception as e:
            print(e)
            return None