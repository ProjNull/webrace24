
from Database.UserModel import Users
from contextlib import contextmanager
from Database.Database import Session


def getAllowed(request):
    if request.method != "GET": return {"message": "Only GET allowed!", "status": 400}

def postAllowed(request):
    if request.method != "POST": return {"message": "Only POST allowed!", "status": 400}
    
@contextmanager
def get_db() -> Session:
    db = Session()  # Create a new database session
    try:
        yield db  # Provide the session to the route function
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()  # Close the session after the route function is done

def missing_params(*params):
    return not (None in params)
    
def formCommit(firstName, lastName, email, phone, githubUrl, preferences, other):
    details = Users(firstName=firstName, lastName=lastName, email=email, phone=phone, githubUrl=githubUrl, preferences=preferences, other=other)
    
    try:
        with get_db() as session:
            User_exists = session.query(Users).filter_by(email=email).first()
            if not User_exists is None: return None
            
            session.add(details)
            session.commit()
            return details.Id
    except:
        return None

def getAUsers(token):
    
    try: 
        with get_db() as session:
            users = session.query(Users).all()
            return users
    except:
        return None