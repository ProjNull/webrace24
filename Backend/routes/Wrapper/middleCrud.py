import base64

def missing_params(*params):
    return not (None in params)

def createToken(username, password):
    passname = username + password
    token = base64.b64encode(passname)
    return str(token)
    