import json

class Response():

    def __init__(self, transport):
        self.transport = transport
        self.status = 200
        self.statusText = "OK"
        self.contentType = "text/plain"
        self.connection = "close"

    def generate_headers(self):
        return f'HTTP/1.1 {self.status} {self.statusText}\r\nContent-Type:{self.contentType}\r\nConnection:{self.connection}\r\n\r\n'

    def write(self, body):
        resp_headers = self.generate_headers()
        self.transport.write((resp_headers + body).encode())

    def send(self, body):
        resp_headers = self.generate_headers()
        self.transport.write((resp_headers + body).encode())
        self.transport.close()

    def json(self, body):
        self.contentType = "application/json"
        resp_headers = self.generate_headers()
        self.transport.write((resp_headers + json.dumps(body)).encode())
        self.transport.close()

    def end(self):
        self.transport.close()
