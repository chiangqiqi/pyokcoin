import requests
import hashlib


def build_sign(params,secret_key):
    sign = ''
    for key in sorted(params.keys()):
        sign += key + '=' + str(params[key]) +'&'

    bytes = (sign+'secret_key='+secret_key).encode('utf-8')
    return  hashlib.md5(bytes).hexdigest().upper()

class OKCoinReq:
    """
    发起请求
    """
    baseurl = "https://www.okcoin.cn/api/v1/"
    def __init__(self, pkey, skey):
        """
        pkey: public key
        skey: secret key
        """
        self.pubilic_key = pkey
        self.secret_key = skey

    def _get_path(self, subpath):
        return self.baseurl + subpath

    def get(self, subpath, params):
        path = self._get_path(subpath)

    def post(self, subpath, params):
        """
        params: dict of the data
        """
        path = self._get_path(subpath)
        sign = build_sign(params, self.secret_key)
        params['sign'] = sign
        resp = requests.post(path, json=params)
        return resp.json()

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
