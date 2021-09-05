from enum import Enum
from typing import List

from bson.objectid import ObjectId
from flask import Flask
from pymongo import MongoClient, message
from pymongo.results import DeleteResult, InsertOneResult, UpdateResult

USERNAME_KEY = 'user'
PWD_KEY = 'pwd'

COIN_USER_KEY = 'user'
COIN_CGID_KEY = 'cgid'
COIN_SYMBOL_KEY = 'symbol'
COIN_AMOUNT_KEY = 'amount'
COIN_PRICE_KEY = 'price'
COIN_WALLET_TYPE_KEY = 'wallet_type'


class Status(Enum):
    SUCCESS = 'success'
    ERROR = 'error'


class DB(object):
    """Database."""

    def __init__(self, mongo_uri: str, server: Flask = None):
        super(DB, self).__init__()
        self._db = MongoClient(mongo_uri).coinkit
        self._server = server

    def add_coin(self, coin_data: dict) -> tuple:
        status = Status.SUCCESS.value
        data = None
        message = 'Added coin successfully'
        try:
            self._db.portfolio.insert_one(coin_data)
        except Exception as e:
            status = Status.ERROR.value
            message = f'Add coin error: {e}'
        return status, data, message

    def update_coin(self, coin_data: dict) -> tuple:
        status = Status.SUCCESS.value
        data = None
        message = 'Updated coin successfully'
        try:
            self._db.portfolio.update_one(
                {
                    COIN_USER_KEY: coin_data[COIN_USER_KEY],
                    COIN_SYMBOL_KEY: coin_data[COIN_SYMBOL_KEY],
                },
                {'$set': coin_data},
            )
        except Exception as e:
            status = Status.ERROR.value
            message = f'Update coin error: {e}'
        return status, data, message

    def delete_coin(self, user: str, symbol: str) -> tuple:
        status = Status.SUCCESS.value
        data = None
        message = 'Deleted coin successfully'
        try:
            self._db.portfolio.delete_one(
                {
                    COIN_USER_KEY: user,
                    COIN_SYMBOL_KEY: symbol,
                }
            )
        except Exception as e:
            status = Status.ERROR.value
            message = f'Delete coin error: {e}'
        return status, data, message

    def ls_coins(self, user: str) -> tuple:
        status = Status.SUCCESS.value
        data = []
        message = 'Listed coin successfully'
        try:
            for t in self._db.portfolio.find({COIN_USER_KEY: user}):
                t.pop('_id')
                data.append(t)
        except Exception as e:
            status = Status.ERROR.value
            message = f'List coin error: {e}'
        return status, data, message if data else 'User not found'
