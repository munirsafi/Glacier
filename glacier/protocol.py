from datetime import datetime
from .routing import Router, routes

import asyncio

class HTTPProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport

    def parse_headers(self, header_string):
        header_obj = {}
        headers = header_string.decode().split("\r\n\r\n")[0]
        fields = headers.split("\r\n")
        route = fields[0].split(' ')
        
        header_obj['Method'], header_obj['Path'], header_obj['Protocol'] = route[0], route[1], route[2]
        for header in fields[1:]:
            key, value = header.split(":", 1)
            header_obj[key] = value.strip()

        return header_obj

    def data_received(self, data):
        headers = self.parse_headers(data)
        origin = self.transport.get_extra_info('socket').getpeername()
        print(f'[{datetime.now()}] [{headers["Method"]}] Request from {origin[0]}, fetching {headers["Path"]}')
        if(routes.get(headers["Path"]) != None):
            routes[headers["Path"]](None, self.transport)
        else:
            self.transport.write('HTTP/1.1 404 Not Found\r\n\n'.encode())
            self.transport.close()
