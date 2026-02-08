import re

def validate_username(username):
    return re.match("^[a-zA-Z0-9_]{4,20}$", username)

def validate_password(password):
    if len(password) < 8:
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[@#$%!]", password):
        return False
    return True
