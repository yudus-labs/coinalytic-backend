from typing import List

from bson.objectid import ObjectId
from flask import Flask
from pymongo import MongoClient
from pymongo.results import DeleteResult, UpdateResult

USERS_KEY = 'users'
USERNAME_KEY = 'user'
PWD_KEY = 'pwd'

PORTFOLIO_KEY = 'portfolio'
PORTFOLIO_CGID_KEY = 'cgid'
PORTFOLIO_NAME_KEY = 'name'
PORTFOLIO_AMOUNT_KEY = 'amount'
PORTFOLIO_PRICE_KEY = 'price'
WALLET_TYPE_KEY = 'wallet_type'


class DB(object):
    """Database."""

    def __init__(self, mongo_uri: str, server: Flask = None):
        super(DB, self).__init__()
        self._db = MongoClient(mongo_uri).coinkit
        self._server = server

    def add_coin(self, coin_data: dict) -> ObjectId:
        res = self._db.coins.insert_one(coin_data)

        return res
