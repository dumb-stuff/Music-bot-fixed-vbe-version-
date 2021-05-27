from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route('/')
def index():
    return {"Hi" : "I am okay"}
def run():
    app.run("0.0.0.0",8080)
def keep_alive():
    server = Thread(target=run)
    server.start()