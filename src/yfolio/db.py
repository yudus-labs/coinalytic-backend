from functools import wraps
import mongoengine as me
from .config import load_db_config


def finalize_response(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        try:
            return {'status': 1, 'result': f(*args, **kwds)}
        except Exception as e:
            return {'status': 0, 'result': str(e)}

    return wrapper


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
    cgId = me.StringField()
    name = me.StringField()
    amount = me.FloatField()


@finalize_response
def about() -> str:
    return 'Welcome to yFolio'


@finalize_response
def ls_tokens() -> dict:
    return Tokens.objects()


@finalize_response
def add_token(cg_id: str, name: str, amount: float) -> bool:
    t = Tokens.objects(cgId=cg_id).first()
    if t:
        t.name = name
        t.amount = amount
        t.save()
    else:
        token = Tokens(cgId=cg_id, name=name, amount=amount)
        token.save()
    return True
