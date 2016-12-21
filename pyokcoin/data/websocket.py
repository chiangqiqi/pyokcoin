#!/usr/bin/env python

import asyncio
import websockets
import json

wslink = 'wss://real.okcoin.cn:10440/websocket/okcoinapi'

async def deps_data(event):
    async with websockets.connect(wslink) as websocket:
        await websocket.send(event)
        while(1):
            resp = await websocket.recv()
            print(json.loads(resp)[0]["channel"])

deps_chn = "{'event':'addChannel','channel':'ok_sub_spotcny_btc_depth_20'}"
trades_chn = "{'event':'addChannel','channel':'ok_sub_spotcny_btc_trades'}"

eloop = asyncio.get_event_loop()

# eloop.run_until_complete(deps_data(deps_chn))
eloop.run_until_complete(deps_data(trades_chn))
