# -*- coding: utf-8 -*-
from collections import defaultdict

class TradeData:
    def __init__(self, data):
        """
        吞入一个二维数组
        """
        self.data = data

    def sum(self):
        return sum([x * y for
                    [x,y] in self.data])

    def _quantity(self):
        return [y for [x, y] in self.data]

    def _price(self):
        return [x for [x, y] in self.data]

    def amount_sum(self):
        return sum(self._quantity())

    def avg_price(self):
        return self.sum() / self.amount_sum()

    def price_range(self):
        p= self._price()
        return max(p), min(p)

    def align(self, price):
        """
        align with current trade price
        """
        return [[x-price, y] for [x, y] in self.data]

    def bucket(self, bucket_size = 0.1, price = None):
        if price is None:
            price = min(self._price())

        aligned_data = self.align(price)

        bucket_res = defaultdict(float)
        for [x, y] in aligned_data:
            bucket_res[int(x/bucket_size)] += y
        return sorted(bucket_res.items())
