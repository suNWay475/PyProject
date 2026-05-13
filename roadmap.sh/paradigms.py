# 1. Imperative — Імперативне програмування
# "Говори комп'ютеру що робити крок за кроком"
numbers = [1, 2, 3, 4, 5]
total = 0

for n in numbers:
    total += n

print(total)  # 15
# 2. OOP — Об'єктно-орієнтоване
# "Код організований навколо об'єктів"
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

account = BankAccount(1000)
account.deposit(500)

# 3. Functional — Функціональне
# "Функції як головний інструмент, без зміни даних"
numbers = [1, 2, 3, 4, 5]

# замість циклу — функції
total = sum(numbers)
evens = list(filter(lambda n: n % 2 == 0, numbers))
squares = list(map(lambda n: n ** 2, numbers))

print(total)    # 15
print(evens)    # [2, 4]
print(squares)  # [1, 4, 9, 16, 25]
# 4. Aspect-Oriented — Аспектно-орієнтоване
# "Відокремлення додаткової логіки від основної"
def log(func):           # додаткова логіка (логування)
    def wrapper(*args, **kwargs):
        print(f'Викликаю {func.__name__}')
        return func(*args, **kwargs)
    return wrapper

@log
def add(a, b):           # основна логіка
    return a + b