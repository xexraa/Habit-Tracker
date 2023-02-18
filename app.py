import os
from flask import Flask
from routes import blp
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()



def create_app():
    app = Flask(__name__)    
    client = MongoClient(os.getenv("MONGODB_URI"))
    app.db = client.get_default_database()
    
    app.register_blueprint(blp)
    
    return app