# Wrapper
from Wrapper.middleCrud import (missing_params, formCommit, getAUsers)
# Packages
from flask import render_template, Blueprint, request, jsonify, json
from Database.Database import Session
from werkzeug.exceptions import HTTPException

Form = Blueprint("form", __name__, url_prefix="/form")
session_instance = Session()

@Form.errorhandler(HTTPException)
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

@Form.after_request
def add_header(response):
    """
    Add an Access-Control-Allow-Origin header to the response.

    :param response: The Flask response object.
    """
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "content-type, authorization"
    return response

from jwtFunctions import requires_authorization  # Import here to avoid circular import
from Form import Form

@Form.route("/send", methods=["POST"])
def sendForm():
    
    firstName = request.json.get("firstName")
    lastName = request.json.get("lastName")
    email = request.json.get("email")
    phone = request.json.get("phone")
    githubUrl = request.json.get("githubUrl")
    preferences = request.json.get("preferences")
    other = request.json.get("other")
    
    if missing_params(firstName, lastName): return {"message": "Missing params!", "status": 400}
    
    returnValue = formCommit(firstName, lastName, email, phone, githubUrl, preferences, other)
    
    return {"message": returnValue, "Status": "ok"}

@requires_authorization
@Form.route("/getAllUsers", methods=["POST"])
def getAllUsers():
    
    token = request.json.get("token")
    users = getAUsers(token)
    
    if users != None:
        return jsonify({"status": "ok"}, users)
    
    return jsonify({"Status": 500})