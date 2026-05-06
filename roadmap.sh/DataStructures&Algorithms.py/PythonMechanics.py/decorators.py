from functools import wraps
#Example 1
def decorator(func):
    def wrapper(a, b): # приймає всі аргументи які ми задамо
        return func(a, b)
    return wrapper

@decorator #або decorator(add)
def add(a, b):
    sumed = a + b
    print(sumed)

decorator(add(2,3))

#Example 2

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