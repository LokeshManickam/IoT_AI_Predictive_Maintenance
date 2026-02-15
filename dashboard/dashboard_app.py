from flask import Flask, render_template
import requests

app = Flask(__name__)

SERVER_URL = "http://127.0.0.1:5000/latest"

@app.route("/")
def dashboard():
    response = requests.get(SERVER_URL)
    data = response.json()
    return data

if __name__ == "__main__":
    app.run(port=7000)
