from sql import check_password, get_user, get_user_by_username
from graphql_schemes.user import AuthenticationNode
from graphql_schemes.error import ErrorNode
import os
import jwt


def authentication_user(email: str, password: str) -> AuthenticationNode:
    token = ""
    text = ""
    error = False
    if check_password(password=password, email=email):
        user = get_user(email=email)
        if user is None:
            user = get_user_by_username(username=email)

        payload = {
            "email": user.email,
            "password": user.password
        }
        token = jwt.encode(payload=payload, key=os.getenv(key='SECRET_KEY', default="11001100"),
                           algorithm=os.getenv(key='ALGORITHM', default='HS256'))
    else:
        text = "Password or username incorrect"

    if text != "":
        error = True

    return AuthenticationNode(token=token, error=ErrorNode(error=error, message=text))
