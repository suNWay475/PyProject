
squeres_cube = (n**3 for n in range(10))
for n in squeres_cube:
    print(n)

data = 'golf'
list = list(data[i] for i in range(len(data) -1, -1, -1))
print(list)

def counter():
    n = 0
    while True:       # нескінченний цикл
        yield n       # але видає по одному
        n += 1

gen = counter()
print(next(gen))  # 0
print(next(gen))  # 1
print(next(gen))  # 2

def evens_gen(n):
    for i in range(n):
        if i % 2 == 0:
            yield i


for n in evens_gen(20):
    print(n)