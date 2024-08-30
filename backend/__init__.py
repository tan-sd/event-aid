from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv


load_dotenv()
app = Flask(__name__)
DB_URI = os.environ["DB_URI"]
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI


db = SQLAlchemy(app)
CORS(app)

routes =[]
for route in routes:
    app.register_blueprint(route)

from routes import *
app.register_blueprint(all_routes)
