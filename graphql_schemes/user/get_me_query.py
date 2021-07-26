from sql import email_is_already, check_hash_password, get_user
from graphql_schemes.user import UserNode
import jwt
import os


def get_me(token: str) -> UserNode:
    token = token.split('JWT ')[1]
    decode_token = jwt.decode(token, os.getenv(key='SECRET_KEY', default="11001100"),
                              algorithms=[os.getenv(key='SECRET_KEY', default="ALGORITHM")])
    if email_is_already(email=decode_token['email']):
        if check_hash_password(hash_password=decode_token['password'], email=decode_token['email']):
            user = get_user(email=decode_token['email'])
            if user:
                return UserNode(username=user.username, email=user.email, first_name=user.first_name)
    return UserNode(username="", email="", first_name="")
