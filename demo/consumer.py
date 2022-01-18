from channels.generic.websocket import WebsocketConsumer,AsyncConsumer
from random import randint
from time import sleep
import json
from .views import *
import asyncio
class GraphConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        self.connected = True
        print("connected", event)
        # await self.send({
        #     "type": "websocket.accept"
        # })

        while self.connected:
            await self.accept()
            await self.send(json.dumps({
                'ram': getRamInfo()
            }))
            await asyncio.sleep(2)

    async def websocket_receive(self, event):
        print("receive", event)

    async def websocket_disconnect(self, event):
        print("disconnected", event)
        self.connected = False

# class GraphConsumer(AsyncConsumer):
#     def connect(self):
#         self.accept()
#         for i in range(1000):
#             v = randint(5,100)
#             self.send(json.dumps({
#                 'ram': getRamInfo() ,
#                 'max': 100 - v 
#             }))
#             sleep(3)


# class GraphConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         await self.accept()
#         for i in range(1000):
#             await self.send(json.dumps({'value':randint(1,9999)}) )
#             sleep(1.5)