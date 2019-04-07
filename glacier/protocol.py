from .routing import Router, routes
from .request import Request
from .response import Response

import asyncio

class HTTPProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        request = Request(self.transport, data)
        response = Response(self.transport)
        if(routes.get(request.path) != None):
            routes[request.path](request, response)
        else:
            self.transport.write('HTTP/1.1 404 Not Found\r\n\n'.encode())
            self.transport.close()
