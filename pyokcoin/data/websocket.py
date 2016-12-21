#!/usr/bin/env python

import asyncio
import websockets
import json
import pandas as pd

wslink = 'wss://real.okcoin.cn:10440/websocket/okcoinapi'

class TradesData(object):
    def __init__(self, data):
        "docstring"
        self.df = pd.DataFrame(data, columns=['id', 'price', 'quantity', 'time','action'])

        self.df['price'] = self.df['price'].astype('float64') 
        self.df.quantity = self.df.quantity.astype('float64')
        self.df["jiaoyie"] = self.df.price * self.df.quantity

    def quantity(self):
        return self.df.groupby("action")["quantity"].sum().to_dict()

    def jiaoyie(self):
        return self.df.groupby("action")["jiaoyie"].sum().to_dict()

    def price(self):
        return self.df.jiaoyie.sum() / self.df.quantity.sum()

def process_data(data):
    td = TradesData(data)
    print(td.quantity())
    print(td.jiaoyie())
    print("price is : {}".format(td.price()))

async def deps_data(event):
    async with websockets.connect(wslink) as websocket:
        await websocket.send(event)
        while(1):
            resp = await websocket.recv()
            rec = json.loads(resp)[0]
            # rec.get("data"))

            if "data" in rec:
                data = rec["data"]
                process_data(data)

# DEPS_CHNu = "{'event':'addChannel','channel':'ok_sub_spotcny_btc_depth_20'}"
trades_chn = "{'event':'addChannel','channel':'ok_sub_spotcny_btc_trades'}"

eloop = asyncio.get_event_loop()

# eloop.run_until_complete(deps_data(deps_chn))
eloop.run_until_complete(deps_data(trades_chn))
