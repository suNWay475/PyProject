# for element in [1, 2, 3]:
#     print(element)
# for element in (1, 2, 3):
#     print(element)
# for key in {'one':1, 'two':2}:
#     print(key)
# for char in "123":
#     print(char)

# s = 'abc'

# it = iter(s)

# for _ in s:
#     print(next(it))

class normal:
    def __init__(self, data):
        self.data = data
        self.current = -1  # починаємо перед першим елементом

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1  # рухаємось вперед
        if self.current < len(self.data):
            return self.data[self.current] 
        raise StopIteration  # кінець

rev = normal('spam')
for char in rev:
    print(char)