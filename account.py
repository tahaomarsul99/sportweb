from flask import Blueprint, render_template, request, session , redirect, flash
from werkzeug.security import generate_password_hash, check_password_hash
from cs50 import SQL
db = SQL('sqlite:///sports.db')

account_router = Blueprint('account_router',
                            __name__,
                            static_folder='static', 
                            template_folder='templates' )

@account_router.route('/register', methods=['GET', 'POST'])
def register():
    # GET
    if request.method == 'GET':
        return render_template('register1.html')
    # POST
    name = request.form.get('name' , None)
    email = request.form.get('email' , None)
    password = request.form.get('pass' , None)

    if not name or not email or not password:
        flash('You must provide all fields')
        return render_template('register.html', error=True)

    users = db.execute('SELECT * FROM users WHERE email LIKE ?;', email)
    if len(users) == 1:
        flash('Email already registered')
        return render_template('register1.html', error=True)

    user_id =db.execute(
        "INSERT INTO users (name, email, password) VALUES (?,?,?);",
         name,
         email, 
        generate_password_hash(password)
    )
    return redirect('/login')


@account_router.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    email = request.form.get('email')
    password = request.form.get('password')
    if not email or not password:
        flash('Worng credentials')
        return render_template('login.html', error=True)

    user = db.execute("SELECT * FROM users WHERE email LIKE ?;")
    if len(user) != 1 or not check_password_hash(user[0]['password'], password):
        flash('Worng credentials')
        return render_template('login.html', error=True)
        
    session['user_id'] = user[0]['id']
    session['is_admin'] = user[0]['is_admin']
    return redirect('/')
@account_router.route('/logout')
def logout():
    session.clear()
    return redirect('/')

