import json

config: dict = json.load(open('config.json'))


def save_config():
    with open('config.json', 'w') as f:
        json.dump(config, f)
