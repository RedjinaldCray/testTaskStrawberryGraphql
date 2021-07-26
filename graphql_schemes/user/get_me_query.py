from sql import email_is_already, check_hash_password, get_user
from .user_node import User
import jwt


def get_me(token: str) -> User:
    token = token.split('JWT ')[1]
    decode_token = jwt.decode(token, '#_%^5@ql)w3&er52+f!zndi76(qmqq#yh&6@zy(mo3d_wnvj5e', algorithms=['HS256'])
    print('decode_token', decode_token)
    if email_is_already(email=decode_token['email']):
        if check_hash_password(hash_password=decode_token['password'], email=decode_token['email']):
            user = get_user(email=decode_token['email'])
            return User(username=user.username, email=user.email, first_name=user.first_name)
    return User(username="", email="", first_name="")
