from flask import Flask, jsonify, request, json
from Wrapper.middleCrud import createToken, postAllowed
from werkzeug.exceptions import HTTPException

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key' 

# Blueprint imports
from Form import Form
app.register_blueprint(Form, url_prefix="/form")

@app.errorhandler(HTTPException)
def handle_exception(e):
    """
    Handle HTTP exceptions by returning JSON responses.

    :param e: The HTTPException to handle.
    """
    response = e.get_response()
    response.data = json.dumps(
        {
            "code": e.code,
            "name": e.name,
            "description": e.description,
        }
    )
    response.content_type = "application/json"
    return response

@app.after_request
def add_header(response):
    """
    Add an Access-Control-Allow-Origin header to the response.

    :param response: The Flask response object.
    """
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "content-type, authorization"
    return response

@app.route("/")
def index():
    return jsonify("hi")

@app.route("/login", methods=["POST"])
def login():
    postAllowed(request)
    
    name = request.json.get("name")
    password = request.json.get("password")
    from jwt import generate_jwt
    return jsonify(
                {
                    "token": generate_jwt({"User_ID": 1}), # TODO: Fetch ID of admin from DB
                    "message": "Sign in successfull",
                }
            )

if __name__ == "__main__":
    app.run("0.0.0.0", 8000)