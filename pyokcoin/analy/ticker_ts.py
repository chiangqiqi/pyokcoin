import pandas as pd
from datetime import datetime
from trade_data import TradeData
from  collections import namedtuple
import json

class Ticker(object):
    def __init__(self, jsonstr):
        "init from json string"
        parsed = json.loads(jsonstr)
        self.buyer = parsed["buy"]
        self.seller = parsed["sell"]
        self.high = parsed["high"]
        self.low = parsed["low"]
        self.last = parsed["last"]
        self.vol = parsed["vol"]

    def diff(self):
        return self.high - self.low

class TimeSliceFactory(object):
    def __init__(self, datadict):
        """
        Keyword Arguments:
        datadict -- the data given
        """
        self.dt = datetime.fromtimestamp(int(datadict[["date"]]))
        self.asks = TradeData(datadict["deps"]["asks"])
        self.bids = TradeData(datadict["deps"]["bids"])
        self.ticker = Ticker(datadict["ticker"])
