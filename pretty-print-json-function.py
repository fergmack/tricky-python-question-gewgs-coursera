# dictionary to json object. use loads() to convert a json string to a python dictionary

import json
def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)
