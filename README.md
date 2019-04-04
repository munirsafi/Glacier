# Glacier: A Lightweight Python Web Framework

Glacier is a lightweight web framework being worked on purely for educational purposes and to better understand the development of web architecture in the Python language. Glacier utilizes the asyncio module to run all requests through an event loop powered by uvloop.

**Example:**

```python
from glacier.server import Glacier

app = Glacier()

@app.route("/", "GET")
def index(request, response):
        response.write('HTTP/1.1 200 OK\r\nContent-Type:text/plain\r\nConnection:close\r\n\r\nTest, World!'.encode())
        response.close()

if __name__ == "__main__":
    app.listen("localhost", 4000)
```