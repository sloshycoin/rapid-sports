from json import dump
from functools import wraps

def doc_response(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        file_path = str(func.__name__).replace('test_','') + 'response.json'
        with open(file_path, 'w') as f:
            dump(result, f)
        return result
    return wrapper
