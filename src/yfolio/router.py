from flask import request
from flask_cors import cross_origin
from . import db


def attach(app):
    @app.route('/about')
    @cross_origin()
    def about():
        return db.about()

    @app.route('/tokens')
    @cross_origin()
    def tokens():
        return db.ls_tokens()

    @app.route('/addToken', methods=['POST'])
    @cross_origin()
    def add_token():
        if request.method == 'POST':
            cg_id = request.args.get('cgId', type=str)
            name = request.args.get('name', type=str)
            amount = request.args.get('amount', type=float)
            db.add_token(cg_id=cg_id, name=name, amount=amount)
            return 'Succeed'
        else:
            return 'Failed'
