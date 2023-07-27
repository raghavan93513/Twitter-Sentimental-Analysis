from flask import Flask, render_template, request, send_file
import os

# Import your IPython Notebook code here, for example:
from get_tweets import get_tweets
app = Flask(__name__, template_folder='templates')

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    topic = request.form["topic"]
    result = get_tweets(topic)
    return result.to_json()

@app.route('/bar')
def bar():
    image_path = os.path.join(app.root_path, 'static', 'bar.png')
    return send_file(image_path, mimetype='image/png')

if __name__ == "__main__":
    app.run()
