from models.user import UserModel
from werkzeug.security import safe_str_cmp


def authenticate(username, password):
    
    user = UserModel.search_username(username)
    
    if user and safe_str_cmp(user.password, password):
        return user

def identity(data):
    uid = data['identity']
    return UserModel.search_id(uid)