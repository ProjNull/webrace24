
from Database.UserModel import Users

def missing_params(*params):
    return not (None in params)
    
def formCommit(firstName, lastName, email, phone, githubUrl, preferences, message, other, session_instance):
    details = Users(firstName=firstName, lastName=lastName, email=email, phone=phone, githubUrl=githubUrl, preferences=preferences, message=message, other=other)
            
    session_instance.add(details)
    session_instance.commit()
    return details.Id

def getAUsers(session_instance):
    users = session_instance.query(Users).all()
    return users
