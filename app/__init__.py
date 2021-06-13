
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from .config import Config

#-----------------------------------------
app = Flask(__name__)

db = SQLAlchemy(app)

# Flask-Login login manager
login = LoginManager()
login.init_app(app)
login.login_view = 'login'

app.config.from_object(Config)
from app import routes