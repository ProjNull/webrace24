from flask import Flask, jsonify

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key' 

# Blueprint imports
from Form import Form
app.register_blueprint(Form, url_prefix="/form")

@app.route("/")
def index():
    return jsonify("hi")