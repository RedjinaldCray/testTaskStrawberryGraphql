from sql import check_password, get_user
from graphql_schemes.token_node import Token
import jwt


def authentication_user(email: str, password: str) -> Token:
    token = ""
    if check_password(password=password, email=email):
        user = get_user(email=email)
        payload = {
            "email": user.email,
            "password": user.password
        }
        token = jwt.encode(payload=payload, key='#_%^5@ql)w3&er52+f!zndi76(qmqq#yh&6@zy(mo3d_wnvj5e', algorithm='HS256')

    return Token(token=token)
