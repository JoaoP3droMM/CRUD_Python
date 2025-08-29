from models.user_model import User
from config import db

def create_user(data):
    user = User(name=data['name'], email=data['email'])
    db.session.add(user)
    db.session.commit()
    
    return user

def get_users():
    return User.query.all()


def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return None
    db.session.delete(user)
    db.session.commit()

    return user