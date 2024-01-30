# Wrapper
from Wrapper.middleCrud import (missing_params, formCommit, getAUsers)
# Packages
from flask import render_template, Blueprint, request, jsonify, json
from Database.Database import Session
from werkzeug.exceptions import HTTPException

Form = Blueprint("form", __name__, url_prefix="/form")
session_instance = Session()

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
    message = request.json.get("message")
    other = request.json.get("other")
    
    if missing_params(firstName, lastName): return {"message": "Missing params!", "status": 400}
    
    returnValue = formCommit(firstName, lastName, email, phone, githubUrl, preferences, message, other, session_instance)
    
    return {"message": returnValue, "Status": "ok"}

@Form.route("/getAllUsers", methods=["GET"])
def getAllUsers():
    users = getAUsers(session_instance)
    
    return jsonify({"status": "ok", "users": [user.serialize() for user in users]})
