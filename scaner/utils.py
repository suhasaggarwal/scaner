from flask import request
from functools import wraps

def add_metadata(f):
    @wraps(f)
    def temp(*args, **kwargs):
        result = f(*args, **kwargs)
        if result is None:
            result = {"message": "Not implemented"}
        code = 200
        print(result)
        print(len(result))
        print(code)
        if isinstance(result, tuple):
            code = result[1]
            result = result[0]
        print(result)
        print(code)
        if 'metadata' not in result:
            result['metadata'] = {}
        result['metadata']['url'] = request.url
        result['metadata']['parameters'] = request.values
        return result, code
    return temp
    
