from ruamel.yaml import YAML

def load_config(cfg_path: str) -> dict:
    """
    Config format:
        {
            'MONGODB': {
                'DB': 'yfolio'
                'HOST': 'localhost'
                'PORT': 27017
                'USERNAME': ''
                'PASSWORD': ''
            }
        }
    """
    cfg_path = str(cfg_path)
    cfg_dict = None
    with open(cfg_path, 'r') as cfg_file:
        cfg_dict = YAML().load(cfg_file)
    return cfg_dict


def load_db_config(cfg_path: str) -> dict:
    cfg = load_config(cfg_path)
    assert cfg, 'Config not found'
    return cfg['MONGODB']
