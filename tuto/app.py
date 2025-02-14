from flask import Flask, session
from flask_bootstrap import Bootstrap5
from flask_login import LoginManager

app = Flask(__name__)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
bootstrap = Bootstrap5(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

import os.path
def mkpath(p):
    return os.path.normpath (
        os.path.join(
            os.path.dirname ( __file__ ),
            p))

from flask_sqlalchemy import SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "sqlite:///"+ mkpath("../myapp.db"))
db = SQLAlchemy(app)

app. config['SECRET_KEY'] = "3d02d25c-55ef-406a-b13d-666ef614b30c"

flash_messages_cleared = False 
@app.before_request
def clear_flash_messages():
    """Efface uniquement les messages flash pour chaque utilisateur, une seule fois par session"""
    global flash_messages_cleared
    if not flash_messages_cleared:
        session.pop('_flashes', None)
        flash_messages_cleared = True