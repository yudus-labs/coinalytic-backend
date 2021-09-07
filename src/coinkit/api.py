import json
from enum import Enum

from flask import Flask, request
from flask_cors import cross_origin

from .db import (
    DB,
    COIN_USER_KEY,
    COIN_AMOUNT_KEY,
    COIN_CGID_KEY,
    COIN_SYMBOL_KEY,
    COIN_PRICE_KEY,
    COIN_WALLET_TYPE_KEY,
    PWD_KEY,
    USERNAME_KEY,
)

PORTFOLIO_DATA_COINS_KEY = 'coins'
PORTFOLIO_DATA_BASE_CURRENCIES_KEY = 'base_currencies'


class Status(Enum):
    SUCCESS = 'success'
    ERROR = 'error'


class ApiHandler(object):
    """Handle public APIs."""

    def __init__(self, server: Flask, db: DB):
        super(ApiHandler, self).__init__()
        self._server = server
        self._db = db

    def validate_coin_data(self, coin_data: str) -> tuple:
        status = Status.ERROR.value
        data = {}
        message = (
            f"Invalid coin data, please provide '{COIN_USER_KEY}' and '{COIN_SYMBOL_KEY}' info"
        )
        try:
            coin_data = json.loads(coin_data)
            if COIN_USER_KEY in coin_data and COIN_SYMBOL_KEY in coin_data:
                if coin_data[COIN_USER_KEY] and coin_data[COIN_SYMBOL_KEY]:
                    data = coin_data
                    status = Status.SUCCESS.value
                    message = 'Valid coin data'
        except Exception as e:
            self._server.logger.debug(f'Coin data invalid: {coin_data}')
            self._server.logger.debug(f'--Error: {e}')
            message = f'Invalid coin data, error: {e}'
        return status, data, message

    def validate_portfolio(self, portfolio_data: str) -> dict:
        status = Status.ERROR.value
        data = {}
        message = f"Invalid portfolio data, please provide '{PORTFOLIO_DATA_COINS_KEY}' and '{PORTFOLIO_DATA_BASE_CURRENCIES_KEY}' info"
        try:
            tmp = json.loads(portfolio_data)
            if PORTFOLIO_DATA_COINS_KEY in tmp and PORTFOLIO_DATA_BASE_CURRENCIES_KEY in tmp:
                data = tmp
                status = Status.SUCCESS.value
                message = 'Valid portfolio data'
        except Exception as e:
            self._server.logger.debug(f'Portfolio data invalid: {portfolio_data}')
            self._server.logger.debug(f'--Error: {e}')
            message = f'Invalid portfolio data, error: {e}'

        return status, data, message

    def register_api(self):
        @self._server.route('/about')
        @cross_origin()
        def about():
            return {
                'status': Status.SUCCESS.value,
                'data': {},
                'message': self._server.config['ABOUT'],
            }

        @self._server.route('/add_coin', methods=['POST'])
        @cross_origin()
        def add_coin():
            coin_data = request.args.get('coin_data', type=str)
            self._server.logger.debug('Add coin:')
            self._server.logger.debug(f'--Coin data: {coin_data}')

            status, data, message = self.validate_coin_data(coin_data)
            if data:
                status, data, message = self._db.add_coin(data)

            return {'status': status, 'data': data, 'message': message}

        @self._server.route('/update_coin', methods=['POST'])
        @cross_origin()
        def update_coin():
            coin_data = request.args.get('coin_data', type=str)
            self._server.logger.debug('Update coin:')
            self._server.logger.debug(f'--Coin data: {coin_data}')

            status, data, message = self.validate_coin_data(coin_data)
            if data:
                status, data, message = self._db.update_coin(data)

            return {'status': status, 'data': data, 'message': message}

        @self._server.route('/delete_coin', methods=['POST'])
        @cross_origin()
        def delete_coin():
            user = request.args.get(COIN_USER_KEY, type=str)
            symbol = request.args.get(COIN_SYMBOL_KEY, type=str)

            self._server.logger.debug('Delete coin:')
            self._server.logger.debug(f'--User: {user}')
            self._server.logger.debug(f'--Symbol: {symbol}')

            if user and symbol:
                status, data, message = self._db.delete_coin(user, symbol)

            else:
                status = Status.ERROR.value
                data = {}
                message = 'Please provide username and coin symbol'

            return {'status': status, 'data': data, 'message': message}

        @self._server.route('/load_portfolio', methods=['GET'])
        @cross_origin()
        def load_portfolio():
            user = request.args.get(COIN_USER_KEY, type=str)

            self._server.logger.debug('Load portfolio:')
            self._server.logger.debug(f'--User: {user}')

            if user:
                status, coins, message = self._db.ls_coins(user)
                data = {PORTFOLIO_DATA_COINS_KEY: coins, PORTFOLIO_DATA_BASE_CURRENCIES_KEY: []}
                if coins:
                    message = 'Loaded portfolio'
                else:
                    message = 'Empty portfolio'

            else:
                status = Status.ERROR.value
                data = {}
                message = 'Please provide username'

            return {'status': status, 'data': data, 'message': message}

        @self._server.route('/save_portfolio', methods=['POST'])
        @cross_origin()
        def save_portfolio():
            user = request.args.get(COIN_USER_KEY, type=str)
            portfolio_data = request.args.get('portfolio_data', type=str)

            self._server.logger.debug('Save portfolio:')
            self._server.logger.debug(f'--User: {user}')

            status, portfolio_data, message = self.validate_portfolio(portfolio_data)

            if user:
                if portfolio_data:
                    for coin in portfolio_data[PORTFOLIO_DATA_COINS_KEY]:
                        self._db.update_coin(coin)
                    data = {}
                    message = 'Saved portfolio'

            else:
                status = Status.ERROR.value
                data = {}
                message = 'Please provide username'

            return {'status': status, 'data': data, 'message': message}
