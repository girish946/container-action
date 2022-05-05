#!/usr/bin/env python3

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route(
    "/",
    methods=[
        "GET",
        "POST",
    ],
)
def hello_world():
    user_name = request.headers.get("user-name")
    data = request.json
    print(data)
    if user_name:
        return f"Hello, {user_name}"
    return "Hello World!"


if __name__ == "__main__":
    app.run(port=5000)
