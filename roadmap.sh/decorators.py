from functools import wraps

def decorator(func):
    @wraps(func)  # запамятай своє ім'я
    def wrapper(*args, **kwargs): # приймає всі аргументи які ми задамо
        return func(*args, **kwargs)
    return wrapper

@decorator
def add(a, b):
    return a + b

print(add.__name__)  # add  ✅ — ім'я збереглось!