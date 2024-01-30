from flask import Flask, jsonify, request

from Wrapper.middleCrud import createToken

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key' 

# Blueprint imports
from Form import Form
app.register_blueprint(Form, url_prefix="/form")

@app.route("/")
def index():
    return jsonify("hi")

@app.route("/login", methods=["POST"])
def login():
    name = request.json.get("name")
    password = request.json.get("password")
    
    token = createToken(name, password)
    # TODO: Make better token
    
    return {"status": "ok", "token": token}

if __name__ == "__main__":
    app.run("0.0.0.0", 8000)