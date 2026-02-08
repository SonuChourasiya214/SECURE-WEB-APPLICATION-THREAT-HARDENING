from flask import session

def regenerate_session():
    session.modified = True
