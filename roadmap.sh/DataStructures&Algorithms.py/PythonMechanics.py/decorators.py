# from functools import wraps

# def decorator(func):
#     @wraps(func)  # запамятай своє ім'я
#     def wrapper(*args, **kwargs): # приймає всі аргументи які ми задамо
#         return func(*args, **kwargs)
#     return wrapper

# @decorator #або decorator(add)
# def add(a, b):
#     return a + b

# print(add.__name__)  # add  ✅ — ім'я збереглось!



def pretty_sumab(func):    # приймає функцію sumab
    def inner(a, b):       # обгортка з тими ж аргументами
        print(str(a) + " + " + str(b) + " is ", end="")  
        # виводить "5 + 3 is " (end="" — без переносу рядка)
        return func(a, b)  # викликає оригінальний sumab
    return inner
@pretty_sumab
def sumab(a, b):
    summed = a + b
    print(summed)  # виводить результат


if __name__ == "__main__": # запустится якщо тільки файл головний !
    sumab(5,3)