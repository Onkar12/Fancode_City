import json

def load_config():
    with open('config/config.json') as config_file:
        return json.load(config_file)

CONFIG = load_config()
