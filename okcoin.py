import urllib.request
import json

class OkCoin(object):
    def __init__(self):
       "some"
       self.root_url = "https://www.okcoin.cn/"

    def query_api(self, api_path):
        url = self.root_url + api_path
        print(url)
        resp = urllib.request.urlopen(url)
        respstr = resp.read()
        return json.loads(respstr.decode())

    def get_ticker(self):
        return self.query_api("api/v1/ticker.do?symbol=btc_cny")

    def get_depth(self):
        return self.query_api("api/v1/depth.do?symbol=btc_cny")

def main():
    okcoin = OkCoin()
    deps = okcoin.get_depth()
    ticker = okcoin.get_ticker()
    print(ticker)
    # print(deps)

if __name__ == '__main__':
    main()
