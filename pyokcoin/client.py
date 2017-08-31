import requests
from .api import OKCoinReq

class OKCoinClient:
    def __init__(self, pkey, skey):
        """
        pkey: public key
        skey: secret key
        """
        self.api = OKCoinReq(pkey, skey)
        self.pubilic_key = pkey
        self.secret_key = skey

    def get_account_info(self):
        path = 'userinfo.do'
        resp = self.api.post(path, {'api_key': self.pubilic_key})

        return resp

    def get_depth(self, pair):
        """
        pair: e.g. btc_cny, ltc_cny
        """
        path = 'depth.do'
        return self.api.get(path, {'symbol': pair})

    def trade(self, pair, price, amount, action):
        """
        api_key: apikey
        symbol: e.g. ltc_cny
        price: price
        amount: amount
        type: buy, sell, buy_market, sell_market
        """
        path = 'trade.do'
        params = {'api_key': self.pubilic_key, 'symbol': pair,
                  'price': price, 'amount': amount, 'type': action}

        return self.api.post(path, params)
