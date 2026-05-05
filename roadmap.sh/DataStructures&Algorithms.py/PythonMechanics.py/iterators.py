# for element in [1, 2, 3]:
#     print(element)
# for element in (1, 2, 3):
#     print(element)
# for key in {'one':1, 'two':2}:
#     print(key)
# for char in "123":
#     print(char)

s = 'abc'

it = iter(s)

for _ in s:
    print(next(it))

def __init__(self, data):
    self.data = data        # зберігаємо рядок, напр. 'spam'
    self.index = len(data)  # index = 4 (починаємо з кінця)
def __iter__(self):
    return self  # каже "я сам є ітератором"
def __next__(self):
    if self.index == 0:
        raise StopIteration      # елементи скінчились — стоп
    self.index = self.index - 1  # рухаємось назад
    return self.data[self.index] # повертаємо символ