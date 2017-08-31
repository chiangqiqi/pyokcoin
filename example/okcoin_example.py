from pyokcoin import OKCoinClient


pkey = '76e81224-b26d-41d7-a030-b9a73b3b07f8'
skey = 'E527C5D45611BE97743EAC78BB8B511D'

client = OKCoinClient(pkey, skey)

def main():
    # 查看账户剩余CNY
    accinfo = client.get_account_info()
    
    cny = float(accinfo['info']['funds']['free']['cny'])

    # 查询某种币价格 e.g. etc
    etc_depth = client.get_depth('etc_cny')

    # 取 top_asks
    etc_price = etc_depth['asks'][0][0]

    # 作为示例，仅交易 10 元人民币
    total_price = float(max(10, cny))

    # 得到交易数量
    amt = total_price/etc_price

    # buy etc
    resp = client.trade('etc_cny', etc_price, amt, 'buy')
    
if __name__ == '__main__':
    main()
