from glacier.server import Glacier

app = Glacier()

@app.route("/", "GET")
def index(request, response):
        response.write('HTTP/1.1 200 OK\r\nContent-Type:text/plain\r\nConnection:close\r\n\r\Test, World!\r\n\n'.encode())
        response.close()

if __name__ == "__main__":
    app.listen("localhost", 4000)
