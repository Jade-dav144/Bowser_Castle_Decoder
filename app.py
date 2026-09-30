from flask import Flask, render_template
import os

app = Flask(__name__)

PYTHON_FILE = "bowser_castle_decoder.py"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCRIPT_PATH = os.path.join(BASE_DIR, PYTHON_FILE)


@app.route("/")
def index():
    with open(SCRIPT_PATH, "r", encoding="utf-8") as file:
        source_code = file.read()

    return render_template(
        "index.html",
        python_file=PYTHON_FILE,
        source_code=source_code
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000))
    )