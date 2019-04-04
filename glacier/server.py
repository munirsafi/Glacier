from datetime import datetime
from functools import wraps
from .routing import Router
from .protocol import HTTPProtocol

import asyncio
import uvloop

class Glacier():

    def __init__(self):
        self.router = Router()
    
    def route(self, path, method=None):
        if(path == None): raise ValueError("A route must be provided")
        def route_handler(func):
            self.router.add(path, func, method)
            def route_add():
                pass
            return route_add
        return route_handler
        
    def listen(self, host="localhost", port=4200):
        asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
        loop = asyncio.get_event_loop()
        try:
            print(f'[{datetime.now()}] [INFO] Glacier running on port {port}')
            server = loop.create_server(HTTPProtocol, host=host, port=port)
            http_server = loop.run_until_complete(server)

            loop.run_forever()
        except KeyboardInterrupt:
            pass
