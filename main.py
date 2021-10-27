from flask import Flask, render_template
import server

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/<data>")
def addtoDatabase(data):
    if data != 'favicon.ico':
        server.addData([data])
    return f'{data} inserted'

if __name__ == "__main__":
    app.run()