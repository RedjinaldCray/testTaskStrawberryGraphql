from sql import check_password
import jwt


def authentication_user(email: str, password: str) -> str:
    token = ""
    if check_password(password=password, email=email):
        payload = {
            "email": email,
            "password": password
        }
        token = jwt.encode(payload=payload, key='#_%^5@ql)w3&er52+f!zndi76(qmqq#yh&6@zy(mo3d_wnvj5e', algorithm='HS256')

    return token
