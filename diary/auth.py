from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/sign-up')
def sign_up():
    return '<h1>Sign-Up</h1>'

@auth.route('/sign-in')
def sign_in():
    return "<p>Sign-In</p>"

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"