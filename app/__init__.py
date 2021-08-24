from flask import Flask
#from config import Config
import os
app = Flask(__name__)
#app.config.from_object(Config)
app.secret_key = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
from app import routes
