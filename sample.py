from glacier.server import Glacier

app = Glacier()

@app.route("/", "GET")
def index(request, response):
        response.send("testing testing!")

if __name__ == "__main__":
    app.listen("localhost", 4000)
