import urllib.request
import json
from pymongo import MongoClient
from time import sleep

class OkCoin(object):
    def __init__(self):
       "some"
       self.root_url = "https://www.okcoin.cn/"
       self.db = MongoClient("localhost")["okcoin"]

    def query_api(self, api_path):
        url = self.root_url + api_path
        resp = urllib.request.urlopen(url)
        respstr = resp.read()
        return json.loads(respstr.decode())

    def get_ticker(self):
        return self.query_api("api/v1/ticker.do?symbol=btc_cny")

    def get_depth(self):
        return self.query_api("api/v1/depth.do?symbol=btc_cny")

    def save_tiker_data(self):
        coll = self.db.get_collection("ticker_data")
        ticker_data = self.get_ticker()
        deps_data = self.get_depth()
        ticker_data["deps"] = deps_data
        t = ticker_data["date"]
        # save if not exists
        if coll.find_one({"date": t}) is None:
            res = coll.insert_one(ticker_data)
            print(res.inserted_id)

    def run_ticker(self):
        while(1):
            self.save_tiker_data()
            sleep(0.5)

def main():
    okcoin = OkCoin()
    okcoin.run_ticker()

if __name__ == '__main__':
    main()
