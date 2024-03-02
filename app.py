from flask import Flask
import os

app = Flask(__name__)


@app.route("/")
def hello():
    var_value = os.getenv("Environement is", "<ENV variableis not set>")
    return f"<h1>ENV VAR is: {var_value}</h1>"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
