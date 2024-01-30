# Wrapper
from Wrapper.middleCrud import (missing_params, formCommit, getAUsers, getAllowed, postAllowed)
# JWT
from jwt import requires_authorization
# Packages
from flask import render_template, Blueprint, request, jsonify
from Database.Database import Session

Form = Blueprint("form", __name__, url_prefix="/form")
session_instance = Session()

@Form.route("/send", methods=["POST"])
def sendForm():
    postAllowed(request)
    
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
@Form.route("/getAllUsers", methods=["GET"])
def getAllUsers():
    getAllowed(request)
    token = request.json.get("token")
    users = getAUsers(token)
    
    if users != None:
        return jsonify({"status": "ok"}, users)
    
    return {"Status": 500}