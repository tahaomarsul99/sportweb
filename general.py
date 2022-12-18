from flask import Blueprint, render_template, request, session , redirect, flash
from cs50 import SQL
db = SQL('sqlite:///sports.db')
general_router = Blueprint('general_router', __name__,
                            static_folder='static', template_folder='templates')

@general_router.route('/home')
def index():
    return render_template('home.html')
    