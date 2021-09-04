import os.path as osp

ABOUT = 'CoinKit'
LOG_DIR = f'{osp.dirname(osp.abspath(__file__))}/.log'
SERVER_LOG = f'{LOG_DIR}/server.log'
LOG_LEVEL = 'INFO'
MONGO_URI = 'mongodb://localhost:27017/'
# MONGO_URI = 'mongodb://10.0.128.168:27017/'
