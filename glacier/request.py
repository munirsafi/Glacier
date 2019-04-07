from datetime import datetime

class Request():

    def __init__(self, transport, data):
        self.origin = transport.get_extra_info('socket').getpeername()
        self.headers = self.parse_headers(data)
        self.method = self.headers['Method']
        self.path = self.headers['Path']
        self.keepAlive = self.headers['Connection'] == 'keep-alive'

        print(f'[{datetime.now()}] [{self.method}] Request from {self.origin[0]}, fetching {self.path}')


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
