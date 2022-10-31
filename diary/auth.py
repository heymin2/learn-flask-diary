from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/sign-in')
def sign_in():
    return render_template('sign_in.html', user="SemiCircle")

@auth.route('/logout')
def logout():
    return render_template('logout.html')

@auth.route('/sign-up')
def sign_up():
    return render_template('sign_up.html')