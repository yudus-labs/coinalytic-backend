import mongoengine as me
from .config import load_db_config


def connect(cfg_path: str):
    cfg = load_db_config(cfg_path)
    me.connect(
        db=cfg['DB'],
        username=cfg['USERNAME'],
        password=cfg['PASSWORD'],
        host=cfg['HOST'],
        port=cfg['PORT'],
    )


class Tokens(me.Document):
    cg_id = me.StringField()
    amount = me.FloatField()


def ls_tokens():
    return {'tokens': Tokens.objects()}
