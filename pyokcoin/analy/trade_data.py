class TradeData:
    def __init__(self, data):
        """
        吞入一个二维数组
        """
        self.data = data

    def sum(self):
        return sum([x * y for
                    [x,y] in self.data])

    def amount(self):
        return sum([x for [x, y] in self.data])

    def avg_price(self):
        return self.sum() / self.amount()
