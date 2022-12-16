from flask import Blueprint, render_template, request, session , redirect, flash
from database import db

general_router = Blueprint('general_router', __name__,
                            static_folder='static', template_folder='templates')

@general_router.route('/home')
def index():
    return render_template('Home.html')
    