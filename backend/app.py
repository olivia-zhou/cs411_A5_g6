from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/weather", methods=["GET"])
def get_weather():
    zip = request.values.get('zip')
    return {"response": zip}