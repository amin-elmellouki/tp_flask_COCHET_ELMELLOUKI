from flask import Flask
from flask_bootstrap import Bootstrap5
from flask import LoginManager

app = Flask(__name__)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
bootstrap = Bootstrap5(app)
login_manager = LoginManager(app)

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



