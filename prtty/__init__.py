import json
from .logger import logger

def prettify(x, default=repr):
    return json.dumps(x, indent=4, default=default)

def pretty(x, default=repr):
    print(json.dumps(x, indent=4, default=default))
    return True



