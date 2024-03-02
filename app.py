from flask import Flask
import os

app = Flask(__name__)


@app.route("/")
def hello():
    var_value = os.getenv("ENV", "<ENV is not set>")
    return f"<h1> Environment: {var_value}</h1>"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
