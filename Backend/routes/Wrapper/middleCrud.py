
from Database.UserModel import Users
from contextlib import contextmanager
from Database.Database import Session
    
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
    
def formCommit(firstName, lastName, email, phone, githubUrl, preferences, other, session_instance):
    details = Users(firstName=firstName, lastName=lastName, email=email, phone=phone, githubUrl=githubUrl, preferences=preferences, other=other)
            
    session_instance.add(details)
    session_instance.commit()
    return details.Id

def getAUsers(session_instance):
    users = session_instance.query(Users).all()
    return users
