from user import User
from werkzeug.security import safe_str_cmp

users = [
    User(1, 'Alex', 'itvizion'),
    User(2, 'Marius', 'qwerty')
]

user_names = {user.login : user for user in users}
user_id = {user.id : user for user in users}


def authenticate(login, password):
    
    user = user_names.get(login, None)
    
    if user and safe_str_cmp(user.password, password):
        return user

def identity(data):
    uid = data['identity']
    return user_id.get(uid, None)