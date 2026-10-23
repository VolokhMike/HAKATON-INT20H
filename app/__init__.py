import os

from dotenv import load_dotenv
from flask import Flask
from flask_login import LoginManager

from connection import create_tables


load_dotenv()

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]
create_tables()
