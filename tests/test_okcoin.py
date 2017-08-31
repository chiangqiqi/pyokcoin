from pyokcoin.client import build_sign
from pyokcoin.client import OKCoinClient

pkey = 'your-api-key'
skey = 'your-secret-key'

def test_build_sign():
    test_params = {'test': 0}
    res = build_sign(test_params, 'test')

client = OKCoinClient(pkey, skey)

def test_post_api():
    # resp = client.get_account_info()
    # assert resp['result'] == True
    resp = client.trade('btc_cny', 28000, 0.0001, 'sell')


def test_get_api():
    resp = client.get_depth('bcc_cny', )
    
