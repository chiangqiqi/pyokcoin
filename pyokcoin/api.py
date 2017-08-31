"""simple abstraction of the okcoin rest api"""
import hashlib
import requests

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

    def get(self, subpath, params, return_json=True):
        path = self._get_path(subpath)
        resp = requests.get(path, params)

        if return_json:
            return resp.json()
        else:
            return resp.text()

    def post(self, subpath, params, sign=True):
        """
        params: dict of the data
        """
        path = self._get_path(subpath)

        if sign:
            sign = build_sign(params, self.secret_key)
            params['sign'] = sign

        resp = requests.post(path, params)
        return resp.json()
