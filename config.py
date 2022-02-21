import json

global _global_config


def init():
    global _global_config
    with open("config.json", "r") as f:
        _global_config = json.loads(f.read())


def get_value(key):
    try:
        return _global_config[key]
    except Exception as e:
        print(f'读取{key}失败\r\n{type(e)} {str(e)}\r\n')
