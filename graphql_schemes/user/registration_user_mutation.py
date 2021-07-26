from sql import create_user, username_is_already, email_is_already
from graphql_schemes.user.registration_node import RegistrationNode
from graphql_schemes.error.error_type_node import ErrorNode
from models import User


def registration_user(username: str, email: str, password: str, first_name: str) -> RegistrationNode:
    registration = False
    error = False
    text = ""
    hash_password = User.set_password(password=password)
    if not username_is_already(username=username):
        if not email_is_already(email=email):
            user = create_user(username=username, password=hash_password, email=email, first_name=first_name)
            if user:
                registration = True
            else:
                text = "Account was not created"
        else:
            text = "Email is already"
    else:
        text = "Username is already"

    if text != "":
        error = True

    return RegistrationNode(registration=registration, error=ErrorNode(error=error, message=text))
