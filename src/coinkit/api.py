import json
from enum import Enum

from flask import Flask, request
from flask_cors import cross_origin

from .db import (
    DB,
    PORTFOLIO_AMOUNT_KEY,
    PORTFOLIO_CGID_KEY,
    PORTFOLIO_KEY,
    PORTFOLIO_NAME_KEY,
    PORTFOLIO_PRICE_KEY,
    PWD_KEY,
    USERNAME_KEY,
    USERS_KEY,
    WALLET_TYPE_KEY,
)


class Status(Enum):
    SUCCESS = 'success'
    ERROR = 'error'


class ApiHandler(object):
    """Handle public APIs."""

    def __init__(self, server: Flask, db: DB):
        super(ApiHandler, self).__init__()
        self._server = server
        self._db = db

    def register_api(self):
        @self._server.route('/about')
        @cross_origin()
        def about():
            return {
                'status': Status.SUCCESS.value,
                'data': {},
                'message': self._server.config['ABOUT'],
            }
