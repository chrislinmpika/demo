from flask import Flask
import os

app = Flask(__name__)


@app.route("/")
def hello():
    # Get the environment variable and capitalize it
    var_value = os.getenv("ENV", "<ENV is not set>").capitalize()
    # Add an emoji to the message
    emoji = "🚀🚀🚀"  # Rocket emoji as an example
    return f"<h1>{emoji} Environment is {var_value}</h1>"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

