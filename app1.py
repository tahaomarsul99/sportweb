from flask import Flask
from flask_sessions import Session
from account import account_router
from general import general_router

app = Flask(__name__)
    
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
# Session(app)
app.register_blueprint(account_router, url_prefix='')
app.register_blueprint(general_router, url_prefix='')

if __name__ == '__main__':
    app.run(debug=True)

