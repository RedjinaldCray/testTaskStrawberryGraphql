from sql import create_user, username_is_already, email_is_already
from models import User


def registration_user(username: str, email: str, password: str, first_name: str) -> bool:
    hash_password = User.set_password(password=password)
    if not username_is_already(username=username):
        if not email_is_already(email=email):
            user = create_user(username=username, password=hash_password, email=email, first_name=first_name)
            if user:
                return True
    return False
