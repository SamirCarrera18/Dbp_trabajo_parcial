from cgitb import html
from flask import Blueprint, render_template, request

login = Blueprint('login', __name__)

@login.route('/')
def inicio():
    return render_template('login.html')

@login.route('/pedro',methods=['POST'])
def usuario():
    data = {
        'nombreUser' : request.form['email']
    }
    
    return render_template('cv.html', data=data)