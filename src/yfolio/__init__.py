from flask import Flask
from flask_mongoengine import MongoEngine
from .config import load_db_config


def create_app(cfg_path) -> Flask:
    cfg = load_db_config(cfg_path)

    app = Flask(__name__)
    app.config['MONGODB_SETTINGS'] = {
        'db': cfg['DB'],
        'host': cfg['HOST'],
        'port': cfg['PORT'],
        'username': cfg['USERNAME'],
        'password': cfg['PASSWORD'],
    }
    mdb = MongoEngine(app)

    return app
